import json
from datetime import datetime

THRESHOLDS = {
    'newman': {'max_failures': 0, 'max_response_time_ms': 2000},
    'jmeter': {'max_error_rate_pct': 5.0, 'max_avg_response_ms': 2000},
    'cypress': {'max_failures': 0},
    'zap':     {'max_high_alerts': 0, 'max_medium_alerts': 5},
}


def validate_newman(data):
    issues = []
    run = data.get('run', {})
    stats = run.get('stats', {})
    failures = run.get('failures', [])

    failed_tests = stats.get('assertions', {}).get('failed', 0)
    if failed_tests > THRESHOLDS['newman']['max_failures']:
        issues.append(f'Newman: {failed_tests} assertions fallidas (máx permitido: 0)')

    timings = run.get('timings', {})
    avg_response = timings.get('responseAverage', 0)
    if avg_response > THRESHOLDS['newman']['max_response_time_ms']:
        issues.append(f'Newman: tiempo promedio {avg_response}ms supera {THRESHOLDS["newman"]["max_response_time_ms"]}ms')

    for failure in failures:
        name = failure.get('source', {}).get('name', 'desconocido')
        error = failure.get('error', {}).get('message', '')
        issues.append(f'Newman fallo en "{name}": {error}')

    return issues


def validate_jmeter(data):
    issues = []
    samples = data if isinstance(data, list) else data.get('samples', [])

    if not samples:
        return issues

    total = len(samples)
    errors = sum(1 for s in samples if not s.get('success', True))
    error_rate = (errors / total) * 100 if total > 0 else 0

    if error_rate > THRESHOLDS['jmeter']['max_error_rate_pct']:
        issues.append(f'JMeter: tasa de error {error_rate:.1f}% supera {THRESHOLDS["jmeter"]["max_error_rate_pct"]}%')

    avg_response = sum(s.get('elapsed', 0) for s in samples) / total
    if avg_response > THRESHOLDS['jmeter']['max_avg_response_ms']:
        issues.append(f'JMeter: tiempo promedio {avg_response:.0f}ms supera {THRESHOLDS["jmeter"]["max_avg_response_ms"]}ms')

    return issues


def validate_cypress(data):
    issues = []
    stats = data.get('stats', {})

    failures = stats.get('failures', 0)
    if failures > THRESHOLDS['cypress']['max_failures']:
        issues.append(f'Cypress: {failures} tests fallidos')

    failed_tests = data.get('failures', [])
    for test in failed_tests:
        title = test.get('fullTitle', 'desconocido')
        error = test.get('err', {}).get('message', '')
        issues.append(f'Cypress fallo en "{title}": {error}')

    return issues


def validate_zap(data):
    issues = []
    alerts = data.get('site', [{}])[0].get('alerts', [])

    high = sum(1 for a in alerts if a.get('riskcode') == '3')
    medium = sum(1 for a in alerts if a.get('riskcode') == '2')

    if high > THRESHOLDS['zap']['max_high_alerts']:
        issues.append(f'ZAP: {high} alertas HIGH (máx permitido: 0)')
        for alert in alerts:
            if alert.get('riskcode') == '3':
                issues.append(f'  → HIGH: {alert.get("alert")} en {alert.get("url")}')

    if medium > THRESHOLDS['zap']['max_medium_alerts']:
        issues.append(f'ZAP: {medium} alertas MEDIUM (máx permitido: {THRESHOLDS["zap"]["max_medium_alerts"]})')

    return issues


VALIDATORS = {
    'newman':  validate_newman,
    'jmeter':  validate_jmeter,
    'cypress': validate_cypress,
    'zap':     validate_zap,
}


def lambda_handler(event, context):
    suite   = event.get('suite', '').lower()
    payload = event.get('results', {})

    if suite not in VALIDATORS:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Suite desconocida: "{suite}". Válidas: {list(VALIDATORS.keys())}'})
        }

    validator = VALIDATORS[suite]
    issues = validator(payload)
    passed = len(issues) == 0

    result = {
        'suite':     suite,
        'timestamp': datetime.utcnow().isoformat(),
        'status':    'PASS' if passed else 'FAIL',
        'issues':    issues,
        'summary':   f'{suite.upper()} {"pasó" if passed else "falló"} la validación'
    }

    print(json.dumps(result, indent=2))

    return {
        'statusCode': 200 if passed else 422,
        'body':       json.dumps(result)
    }