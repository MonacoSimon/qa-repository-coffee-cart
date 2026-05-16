Started by user simon monaco
Obtained Jenkinsfile from git https://github.com/MonacoSimon/qa-repository-coffee-cart.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/pipeline-coffee-cart
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/jenkins_home/workspace/pipeline-coffee-cart/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/MonacoSimon/qa-repository-coffee-cart.git # timeout=10
Fetching upstream changes from https://github.com/MonacoSimon/qa-repository-coffee-cart.git
 > git --version # timeout=10
 > git --version # 'git version 2.47.3'
 > git fetch --tags --force --progress -- https://github.com/MonacoSimon/qa-repository-coffee-cart.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 12f1c49dac8aefc562e535994ff156c89d5f14b7 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 12f1c49dac8aefc562e535994ff156c89d5f14b7 # timeout=10
Commit message: "cambio rutas en jenkinsfile"
 > git rev-list --no-walk ec27abdf50bd456653f2214345345b57751b9c17 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Clean up previous containers)
[Pipeline] sh
+ docker rm -f api-test-coffee-app
+ docker rm -f jmeter-test-coffee-app
+ docker rm -f zap-test-coffee-app
+ docker rm -f cypress-test-coffee-app
+ docker ps -a --filter name=coffee -q
+ xargs -r docker rm -f
+ docker network rm pipeline-coffee-cart_qa-network
+ true
+ docker network prune -f
+ docker-compose down -v --remove-orphans
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Ejecutar pruebas)
[Pipeline] stage
[Pipeline] { (API Tests Newman)
[Pipeline] catchError
[Pipeline] {
[Pipeline] sh
+ hostname
+ docker run --rm --volumes-from 181c4e6d445a postman/newman:alpine run /var/jenkins_home/workspace/pipeline-coffee-cart/api-testing/postman/collections/api-testing-coffee-cart.postman_collection.json -e /var/jenkins_home/workspace/pipeline-coffee-cart/api-testing/postman/enviroment/environment-coffee-cart.postman_environment.json --env-var urlBase=https://coffee-cart.app/ -r cli,json,junit --reporter-json-export /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/newman/report.json --reporter-junit-export /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/newman/report.xml
newman

api-testing-coffee-cart

❏ collection-of-gets
↳ get-index
  GET https://coffee-cart.app/ [200 OK, 1.33kB, 249ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ cart
  GET https://coffee-cart.app/cart [200 OK, 1.33kB, 58ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ github
  GET https://coffee-cart.app/github [200 OK, 1.33kB, 52ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ breake-cart
  GET https://coffee-cart.app/?breakable=1 [200 OK, 1.33kB, 49ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ app-with-adds
  GET https://coffee-cart.app/?ad=1 [200 OK, 1.33kB, 48ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

┌─────────────────────────┬───────────────────┬───────────────────┐
│                         │          executed │            failed │
├─────────────────────────┼───────────────────┼───────────────────┤
│              iterations │                 1 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│                requests │                 5 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│            test-scripts │                 5 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│      prerequest-scripts │                 0 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│              assertions │                25 │                 0 │
├─────────────────────────┴───────────────────┴───────────────────┤
│ total run duration: 684ms                                       │
├─────────────────────────────────────────────────────────────────┤
│ total data received: 4.69kB (approx)                            │
├─────────────────────────────────────────────────────────────────┤
│ average response time: 91ms [min: 48ms, max: 249ms, s.d.: 78ms] │
└─────────────────────────────────────────────────────────────────┘
[Pipeline] }
[Pipeline] // catchError
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Cypress)
[Pipeline] catchError
[Pipeline] {
[Pipeline] sh
+ docker-compose up --build --abort-on-container-exit cypress-tests
#0 building with "default" instance using docker driver

#1 [cypress-tests internal] load build definition from Dockerfile
#1 transferring dockerfile: 163B done
#1 DONE 0.0s

#2 [cypress-tests internal] load metadata for docker.io/cypress/included:latest
#2 DONE 0.0s

#3 [cypress-tests internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [cypress-tests 1/5] FROM docker.io/cypress/included:latest
#4 DONE 0.0s

#5 [cypress-tests internal] load build context
#5 transferring context: 1.24kB done
#5 DONE 0.0s

#6 [cypress-tests 2/5] WORKDIR /e2e
#6 CACHED

#7 [cypress-tests 4/5] RUN npm ci
#7 CACHED

#8 [cypress-tests 3/5] COPY cypress/package*.json ./
#8 CACHED

#9 [cypress-tests 5/5] COPY cypress/ ./
#9 CACHED

#10 [cypress-tests] exporting to image
#10 exporting layers done
#10 writing image sha256:5dffdbe58d65f67ef29019307a7a87723212aa3d8adc7e660ff327fbdee681ba done
#10 naming to docker.io/library/pipeline-coffee-cart-cypress-tests done
#10 DONE 0.0s
 Network pipeline-coffee-cart_qa-network  Creating
 Network pipeline-coffee-cart_qa-network  Created
 Container api-test-coffee-app  Creating
 Container api-test-coffee-app  Created
 Container cypress-test-coffee-app  Creating
 Container cypress-test-coffee-app  Created
Attaching to cypress-test-coffee-app
[2Kcypress-test-coffee-app  | ❯  Verifying Cypress can run /root/.cache/Cypress/15.15.0/Cypress
[2Kcypress-test-coffee-app  | ✔  Verified Cypress!       /root/.cache/Cypress/15.15.0/Cypress


[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  |   Debug faster with full visibility.
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  |   Record to Cypress Cloud and get instant access to full test details and replays.
[2Kcypress-test-coffee-app  |   Inspect the DOM, network events, and console logs exactly as they ran in CI.
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  |   >> [36mhttps://on.cypress.io/cloud-get-started[39m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [90m----------------------------------------------------------------------------------------------------[39m
cypress-test-coffee-app exited with code 1
Aborting on container exit...
 Container cypress-test-coffee-app  Stopping
 Container cypress-test-coffee-app  Stopped
[Pipeline] }
ERROR: script returned exit code 1
[Pipeline] // catchError
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Jmeter)
[Pipeline] catchError
[Pipeline] {
[Pipeline] sh
+ mkdir -p /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/jmeter
+ hostname
+ docker run --rm --volumes-from 181c4e6d445a --entrypoint /bin/sh justb4/jmeter:latest -c 
                                    found=0
                                    for test in /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/*.jmx; do
                                      [ -f "$test" ] || continue
                                      found=1
                                      filename=$(basename $test .jmx)
                                      timestamp=$(date +%Y%m%d-%H%M%S)
                                      echo Ejecutando: $filename
                                      jmeter -n -f -t $test -l /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/jmeter/$filename.jtl -e -o /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/jmeter/$filename-report-$timestamp -j /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/jmeter/$filename.log
                                      echo Terminado: $filename
                                    done
                                    if [ $found -eq 0 ]; then
                                      echo No se encontraron archivos .jmx
                                      exit 1
                                    fi
                                  
Ejecutando: Test-Plan-100-users
May 16, 2026 8:34:42 PM java.util.prefs.FileSystemPreferences$1 run
INFO: Created user preferences directory.
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-100-users.jmx
Starting standalone test @ May 16, 2026 8:34:43 PM CEST (1778956483832)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     51 in 00:00:16 =    3.2/s Avg:   181 Min:    43 Max:  1314 Err:     0 (0.00%) Active: 3 Started: 27 Finished: 24
summary +     95 in 00:00:30 =    3.2/s Avg:   112 Min:    41 Max:   201 Err:     0 (0.00%) Active: 6 Started: 77 Finished: 71
summary =    146 in 00:00:46 =    3.2/s Avg:   136 Min:    41 Max:  1314 Err:     0 (0.00%)
summary +     54 in 00:00:17 =    3.1/s Avg:   105 Min:    42 Max:   188 Err:     0 (0.00%) Active: 0 Started: 100 Finished: 100
summary =    200 in 00:01:03 =    3.2/s Avg:   127 Min:    41 Max:  1314 Err:     0 (0.00%)
Tidying up ...    @ May 16, 2026 8:35:47 PM CEST (1778956547407)
... end of run
Terminado: Test-Plan-100-users
Ejecutando: Test-Plan-20-users
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-20-users.jmx
Starting standalone test @ May 16, 2026 8:35:51 PM CEST (1778956551923)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     15 in 00:00:08 =    2.0/s Avg:   152 Min:    42 Max:   736 Err:     0 (0.00%) Active: 1 Started: 8 Finished: 7
summary +     25 in 00:00:15 =    1.7/s Avg:   108 Min:    44 Max:   185 Err:     0 (0.00%) Active: 0 Started: 20 Finished: 20
summary =     40 in 00:00:22 =    1.8/s Avg:   124 Min:    42 Max:   736 Err:     0 (0.00%)
Tidying up ...    @ May 16, 2026 8:36:14 PM CEST (1778956574703)
... end of run
Terminado: Test-Plan-20-users
Ejecutando: Test-Plan-50-users
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-50-users.jmx
Starting standalone test @ May 16, 2026 8:36:18 PM CEST (1778956578935)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     21 in 00:00:11 =    1.9/s Avg:   146 Min:    42 Max:   735 Err:     0 (0.00%) Active: 2 Started: 11 Finished: 9
summary +     60 in 00:00:30 =    2.0/s Avg:   111 Min:    42 Max:   199 Err:     0 (0.00%) Active: 3 Started: 42 Finished: 39
summary =     81 in 00:00:41 =    2.0/s Avg:   120 Min:    42 Max:   735 Err:     0 (0.00%)
summary +     19 in 00:00:10 =    1.8/s Avg:   108 Min:    46 Max:   178 Err:     0 (0.00%) Active: 0 Started: 50 Finished: 50
summary =    100 in 00:00:52 =    1.9/s Avg:   118 Min:    42 Max:   735 Err:     0 (0.00%)
Tidying up ...    @ May 16, 2026 8:37:10 PM CEST (1778956630967)
... end of run
Terminado: Test-Plan-50-users
Ejecutando: Test-Plan-80-users
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-80-users.jmx
Starting standalone test @ May 16, 2026 8:37:15 PM CEST (1778956635443)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     39 in 00:00:15 =    2.7/s Avg:   133 Min:    42 Max:   847 Err:     0 (0.00%) Active: 1 Started: 20 Finished: 19
summary +     80 in 00:00:30 =    2.7/s Avg:   109 Min:    41 Max:   208 Err:     0 (0.00%) Active: 1 Started: 60 Finished: 59
summary =    119 in 00:00:45 =    2.7/s Avg:   117 Min:    41 Max:   847 Err:     0 (0.00%)
summary +     41 in 00:00:15 =    2.7/s Avg:   107 Min:    41 Max:   189 Err:     0 (0.00%) Active: 0 Started: 80 Finished: 80
summary =    160 in 00:01:00 =    2.7/s Avg:   114 Min:    41 Max:   847 Err:     0 (0.00%)
Tidying up ...    @ May 16, 2026 8:38:15 PM CEST (1778956695521)
... end of run
Terminado: Test-Plan-80-users
[Pipeline] }
[Pipeline] // catchError
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Zap)
[Pipeline] catchError
[Pipeline] {
[Pipeline] sh
+ docker-compose up --build --abort-on-container-exit zap-tests
#0 building with "default" instance using docker driver

#1 [cypress-tests internal] load build definition from Dockerfile
#1 transferring dockerfile: 163B done
#1 DONE 0.0s

#2 [cypress-tests internal] load metadata for docker.io/cypress/included:latest
#2 DONE 0.0s

#3 [cypress-tests internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [cypress-tests 1/5] FROM docker.io/cypress/included:latest
#4 DONE 0.0s

#5 [cypress-tests internal] load build context
#5 transferring context: 1.24kB done
#5 DONE 0.0s

#6 [cypress-tests 2/5] WORKDIR /e2e
#6 CACHED

#7 [cypress-tests 3/5] COPY cypress/package*.json ./
#7 CACHED

#8 [cypress-tests 4/5] RUN npm ci
#8 CACHED

#9 [cypress-tests 5/5] COPY cypress/ ./
#9 CACHED

#10 [cypress-tests] exporting to image
#10 exporting layers done
#10 writing image sha256:5dffdbe58d65f67ef29019307a7a87723212aa3d8adc7e660ff327fbdee681ba done
#10 naming to docker.io/library/pipeline-coffee-cart-cypress-tests done
#10 DONE 0.0s
 Container api-test-coffee-app  Created
 Container cypress-test-coffee-app  Created
 Container zap-test-coffee-app  Creating
 Container zap-test-coffee-app  Created
Attaching to zap-test-coffee-app
[2Kzap-test-coffee-app  | Using the Automation Framework
[2Kzap-test-coffee-app  | Total of 10 URLs
[2Kzap-test-coffee-app  | PASS: Vulnerable JS Library (Powered by Retire.js) [10003]
[2Kzap-test-coffee-app  | PASS: In Page Banner Information Leak [10009]
[2Kzap-test-coffee-app  | PASS: Cookie No HttpOnly Flag [10010]
[2Kzap-test-coffee-app  | PASS: Cookie Without Secure Flag [10011]
[2Kzap-test-coffee-app  | PASS: Content-Type Header Missing [10019]
[2Kzap-test-coffee-app  | PASS: Information Disclosure - Debug Error Messages [10023]
[2Kzap-test-coffee-app  | PASS: Information Disclosure - Sensitive Information in URL [10024]
[2Kzap-test-coffee-app  | PASS: Information Disclosure - Sensitive Information in HTTP Referrer Header [10025]
[2Kzap-test-coffee-app  | PASS: HTTP Parameter Override [10026]
[2Kzap-test-coffee-app  | PASS: Off-site Redirect [10028]
[2Kzap-test-coffee-app  | PASS: Cookie Poisoning [10029]
[2Kzap-test-coffee-app  | PASS: User Controllable Charset [10030]
[2Kzap-test-coffee-app  | PASS: User Controllable HTML Element Attribute (Potential XSS) [10031]
[2Kzap-test-coffee-app  | PASS: Viewstate [10032]
[2Kzap-test-coffee-app  | PASS: Directory Browsing [10033]
[2Kzap-test-coffee-app  | PASS: Heartbleed OpenSSL Vulnerability (Indicative) [10034]
[2Kzap-test-coffee-app  | PASS: Strict-Transport-Security Header [10035]
[2Kzap-test-coffee-app  | PASS: HTTP Server Response Header [10036]
[2Kzap-test-coffee-app  | PASS: Server Leaks Information via "X-Powered-By" HTTP Response Header Field(s) [10037]
[2Kzap-test-coffee-app  | PASS: X-Backend-Server Header Information Leak [10039]
[2Kzap-test-coffee-app  | PASS: Secure Pages Include Mixed Content [10040]
[2Kzap-test-coffee-app  | PASS: HTTP to HTTPS Insecure Transition in Form Post [10041]
[2Kzap-test-coffee-app  | PASS: HTTPS to HTTP Insecure Transition in Form Post [10042]
[2Kzap-test-coffee-app  | PASS: User Controllable JavaScript Event (XSS) [10043]
[2Kzap-test-coffee-app  | PASS: Big Redirect Detected (Potential Sensitive Information Leak) [10044]
[2Kzap-test-coffee-app  | PASS: X-ChromeLogger-Data (XCOLD) Header Information Leak [10052]
[2Kzap-test-coffee-app  | PASS: Cookie without SameSite Attribute [10054]
[2Kzap-test-coffee-app  | PASS: CSP [10055]
[2Kzap-test-coffee-app  | PASS: X-Debug-Token Information Leak [10056]
[2Kzap-test-coffee-app  | PASS: Username Hash Found [10057]
[2Kzap-test-coffee-app  | PASS: X-AspNet-Version Response Header [10061]
[2Kzap-test-coffee-app  | PASS: PII Disclosure [10062]
[2Kzap-test-coffee-app  | PASS: Timestamp Disclosure [10096]
[2Kzap-test-coffee-app  | PASS: Hash Disclosure [10097]
[2Kzap-test-coffee-app  | PASS: Cross-Domain Misconfiguration [10098]
[2Kzap-test-coffee-app  | PASS: Source Code Disclosure [10099]
[2Kzap-test-coffee-app  | PASS: Weak Authentication Method [10105]
[2Kzap-test-coffee-app  | PASS: Reverse Tabnabbing [10108]
[2Kzap-test-coffee-app  | PASS: Dangerous JS Functions [10110]
[2Kzap-test-coffee-app  | PASS: Authentication Request Identified [10111]
[2Kzap-test-coffee-app  | PASS: Session Management Response Identified [10112]
[2Kzap-test-coffee-app  | PASS: Verification Request Identified [10113]
[2Kzap-test-coffee-app  | PASS: Script Served From Malicious Domain (polyfill) [10115]
[2Kzap-test-coffee-app  | PASS: ZAP is Out of Date [10116]
[2Kzap-test-coffee-app  | PASS: Absence of Anti-CSRF Tokens [10202]
[2Kzap-test-coffee-app  | PASS: Private IP Disclosure [2]
[2Kzap-test-coffee-app  | PASS: Session ID in URL Rewrite [3]
[2Kzap-test-coffee-app  | PASS: Script Passive Scan Rules [50001]
[2Kzap-test-coffee-app  | PASS: Stats Passive Scan Rule [50003]
[2Kzap-test-coffee-app  | PASS: Insecure JSF ViewState [90001]
[2Kzap-test-coffee-app  | PASS: Java Serialization Object [90002]
[2Kzap-test-coffee-app  | PASS: Charset Mismatch [90011]
[2Kzap-test-coffee-app  | PASS: Application Error Disclosure [90022]
[2Kzap-test-coffee-app  | PASS: WSDL File Detection [90030]
[2Kzap-test-coffee-app  | PASS: Loosely Scoped Cookie [90033]
[2Kzap-test-coffee-app  | WARN-NEW: Re-examine Cache-control Directives [10015] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Cross-Domain JavaScript Source File Inclusion [10017] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Missing Anti-clickjacking Header [10020] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: X-Content-Type-Options Header Missing [10021] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-b859522e.css (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/favicon.ico (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Information Disclosure - Suspicious Comments [10027] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-8bfa4912.js (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-8bfa4912.js (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-8bfa4912.js (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-8bfa4912.js (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-8bfa4912.js (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Content Security Policy (CSP) Header Not Set [10038] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Storable and Cacheable Content [10049] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-b859522e.css (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/favicon.ico (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Retrieved from Cache [10050] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-b859522e.css (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/favicon.ico (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Permissions Policy Header Not Set [10063] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Modern Web Application [10109] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Sub Resource Integrity Attribute Missing [90003] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Cross-Origin-Embedder-Policy Header Missing or Invalid [90004] x 15 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?ad=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/robots.txt (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | FAIL-NEW: 0   FAIL-INPROG: 0  WARN-NEW: 12    WARN-INPROG: 0  INFO: 0 IGNORE: 0       PASS: 55
zap-test-coffee-app exited with code 0
Aborting on container exit...
 Container zap-test-coffee-app  Stopping
 Container zap-test-coffee-app  Stopped
[Pipeline] }
[Pipeline] // catchError
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] sh
+ docker-compose down --remove-orphans
 Container zap-test-coffee-app  Stopping
 Container zap-test-coffee-app  Stopped
 Container zap-test-coffee-app  Removing
 Container zap-test-coffee-app  Removed
 Container cypress-test-coffee-app  Stopping
 Container cypress-test-coffee-app  Stopped
 Container cypress-test-coffee-app  Removing
 Container cypress-test-coffee-app  Removed
 Container api-test-coffee-app  Stopping
 Container api-test-coffee-app  Stopped
 Container api-test-coffee-app  Removing
 Container api-test-coffee-app  Removed
 Network pipeline-coffee-cart_qa-network  Removing
 Network pipeline-coffee-cart_qa-network  Removed
[Pipeline] archiveArtifacts
Archiving artifacts
[Pipeline] junit
Recording test results
[Checks API] No suitable checks publisher found.
[Pipeline] echo
Todas las pruebas se ejecutaron correctamente.
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
