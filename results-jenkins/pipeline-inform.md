[Pipeline] sh
+ hostname
+ docker run --rm --volumes-from 181c4e6d445a postman/newman:alpine run /var/jenkins_home/workspace/pipeline-coffee-cart/api-testing/postman/collections/api-testing-coffee-cart.postman_collection.json -e /var/jenkins_home/workspace/pipeline-coffee-cart/api-testing/postman/enviroment/environment-coffee-cart.postman_environment.json --env-var urlBase=https://coffee-cart.app/ -r cli,json,junit --reporter-json-export /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/newman/report.json --reporter-junit-export /var/jenkins_home/workspace/pipeline-coffee-cart/results-docker/newman/report.xml
newman

api-testing-coffee-cart

❏ collection-of-gets
↳ get-index
  GET https://coffee-cart.app/ [200 OK, 1.33kB, 591ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ cart
  GET https://coffee-cart.app/cart [200 OK, 1.33kB, 56ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ github
  GET https://coffee-cart.app/github [200 OK, 1.33kB, 58ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ breake-cart
  GET https://coffee-cart.app/?breakable=1 [200 OK, 1.33kB, 57ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

↳ app-with-adds
  GET https://coffee-cart.app/?ad=1 [200 OK, 1.33kB, 52ms]
  ✓  Es HTML
  ✓  Contiene formulario de reset
  ✓  La respuesta contiene contenido esperado
  ✓  Tiempo de respuesta aceptable
  ✓  La respuesta no está vacía

┌─────────────────────────┬────────────────────┬────────────────────┐
│                         │           executed │             failed │
├─────────────────────────┼────────────────────┼────────────────────┤
│              iterations │                  1 │                  0 │
├─────────────────────────┼────────────────────┼────────────────────┤
│                requests │                  5 │                  0 │
├─────────────────────────┼────────────────────┼────────────────────┤
│            test-scripts │                  5 │                  0 │
├─────────────────────────┼────────────────────┼────────────────────┤
│      prerequest-scripts │                  0 │                  0 │
├─────────────────────────┼────────────────────┼────────────────────┤
│              assertions │                 25 │                  0 │
├─────────────────────────┴────────────────────┴────────────────────┤
│ total run duration: 1017ms                                        │
├───────────────────────────────────────────────────────────────────┤
│ total data received: 4.69kB (approx)                              │
├───────────────────────────────────────────────────────────────────┤
│ average response time: 162ms [min: 52ms, max: 591ms, s.d.: 214ms] │
└───────────────────────────────────────────────────────────────────┘
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

#6 [cypress-tests 4/5] RUN npm ci
#6 CACHED

#7 [cypress-tests 2/5] WORKDIR /e2e
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
[2Kcypress-test-coffee-app  | [35mThe [33mvideoUploadOnPasses[39m[35m configuration option was removed in Cypress version 13.0.0.[39m
[2Kcypress-test-coffee-app  | [35m[39m
[2Kcypress-test-coffee-app  | [35mYou can safely remove this option from your config.[39m
[2Kcypress-test-coffee-app  | [35m[39m
[2Kcypress-test-coffee-app  | [35mhttps://on.cypress.io/migration-guide[39m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [90m====================================================================================================[39m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [0m  ([4m[1mRun Starting[22m[24m)[0m
                                                                      [90m│[39m
[2Kcypress-test-coffee-app  | [90m  │[39m [90mBrowser:[39m        Electron 138 [90m(headless)[39m                                                        [90m│[39m
[2Kcypress-test-coffee-app  | [90m  │[39m [90mNode Version:[39m   [0mv24.15.0 [90m(/usr/local/bin/node)[39m[0m                                                 [90m│[39m
[2Kcypress-test-coffee-app  | [90m  │[39m [90mSpecs:[39m          [0m12 found (accesibility-with-axe.cy.js, add-advertising.cy.js, add-multiple-pro[0m [90m│[39m
[2Kcypress-test-coffee-app  | [90m  │[39m                 [0mducts-to-cart.cy.js, add-product-cart.cy.js, button-add-to-cart.cy.js, change-[0m [90m│[39m
[2Kcypress-test-coffee-app  | [90m  │[39m                 [0mcaffee-title.cy.js, get-a-discount.cy.js, index.cy.js, pay-for-a-product.cy.js[0m [90m│[39m
[2Kcypress-test-coffee-app  | [90m  │[39m                 [0m, pay-hover.cy.js, remo...)[0m                                                    [90m│[39m
[2Kcypress-test-coffee-app  | [90m  │[39m [90mSearched:[39m       [0mcypress**/*.cy.{js,jsx,ts,tsx}[0m                                                 [90m│[39m
[2Kcypress-test-coffee-app  |                                                                                                     
[2Kcypress-test-coffee-app  |   Running:  [90maccesibility-with-axe.cy.js[39m                                                    [90m(1 of 12)[39m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [0m[0m
[2Kcypress-test-coffee-app  | [0m  Accesibilidad - Home[0m
[2Kcypress-test-coffee-app  |   [31m  1) no debería tener errores críticos[0m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [92m [0m[32m 0 passing[0m[90m (5s)[0m
[2Kcypress-test-coffee-app  | [31m  1 failing[0m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [0m  1) Accesibilidad - Home
[2Kcypress-test-coffee-app  |        no debería tener errores críticos:
[2Kcypress-test-coffee-app  | [0m[31m     AssertionError: 1 accessibility violation was detected: expected 1 to equal 0[0m[90m
[2Kcypress-test-coffee-app  |       at Context.eval (webpack://cypress/./node_modules/cypress-axe/dist/index.js:102:0)
[2Kcypress-test-coffee-app  |       at getRet (https://coffee-cart.app/__cypress/runner/cypress_runner.js:122945:20)
[2Kcypress-test-coffee-app  |       at tryCatcher (https://coffee-cart.app/__cypress/runner/cypress_runner.js:1777:23)
[2Kcypress-test-coffee-app  |       at Promise.attempt.Promise.try (https://coffee-cart.app/__cypress/runner/cypress_runner.js:4285:29)
[2Kcypress-test-coffee-app  |       at Context.thenFn (https://coffee-cart.app/__cypress/runner/cypress_runner.js:122956:66)
[2Kcypress-test-coffee-app  |       at Context.then (https://coffee-cart.app/__cypress/runner/cypress_runner.js:123207:21)
[2Kcypress-test-coffee-app  |       at wrapped (https://coffee-cart.app/__cypress/runner/cypress_runner.js:146488:19)
[2Kcypress-test-coffee-app  | [0m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [31m  ([4m[1mResults[22m[24m)[39m
[2Kcypress-test-coffee-app  | 
[2Kcypress-test-coffee-app  | [90m----------------------------------------------------------------------------------------------------[39m
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
May 20, 2026 12:42:39 AM java.util.prefs.FileSystemPreferences$1 run
INFO: Created user preferences directory.
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-100-users.jmx
Starting standalone test @ May 20, 2026 12:42:40 AM CEST (1779230560743)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     60 in 00:00:19 =    3.1/s Avg:   119 Min:    43 Max:   632 Err:     0 (0.00%) Active: 3 Started: 32 Finished: 29
summary +     97 in 00:00:30 =    3.3/s Avg:   120 Min:    42 Max:   916 Err:     0 (0.00%) Active: 5 Started: 82 Finished: 77
summary =    157 in 00:00:49 =    3.2/s Avg:   120 Min:    42 Max:   916 Err:     0 (0.00%)
summary +     43 in 00:00:13 =    3.3/s Avg:   110 Min:    43 Max:   187 Err:     0 (0.00%) Active: 0 Started: 100 Finished: 100
summary =    200 in 00:01:02 =    3.2/s Avg:   118 Min:    42 Max:   916 Err:     0 (0.00%)
Tidying up ...    @ May 20, 2026 12:43:42 AM CEST (1779230622955)
... end of run
Terminado: Test-Plan-100-users
Ejecutando: Test-Plan-20-users
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-20-users.jmx
Starting standalone test @ May 20, 2026 12:43:46 AM CEST (1779230626359)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     25 in 00:00:14 =    1.8/s Avg:   132 Min:    43 Max:   583 Err:     0 (0.00%) Active: 3 Started: 14 Finished: 11
summary +     15 in 00:00:07 =    2.3/s Avg:   105 Min:    39 Max:   181 Err:     0 (0.00%) Active: 0 Started: 20 Finished: 20
summary =     40 in 00:00:20 =    2.0/s Avg:   122 Min:    39 Max:   583 Err:     0 (0.00%)
Tidying up ...    @ May 20, 2026 12:44:07 AM CEST (1779230647182)
... end of run
Terminado: Test-Plan-20-users
Ejecutando: Test-Plan-50-users
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-50-users.jmx
Starting standalone test @ May 20, 2026 12:44:10 AM CEST (1779230650595)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     37 in 00:00:19 =    1.9/s Avg:   123 Min:    41 Max:   511 Err:     0 (0.00%) Active: 2 Started: 20 Finished: 18
summary +     59 in 00:00:31 =    1.9/s Avg:   113 Min:    41 Max:   199 Err:     0 (0.00%) Active: 3 Started: 50 Finished: 47
summary =     96 in 00:00:50 =    1.9/s Avg:   117 Min:    41 Max:   511 Err:     0 (0.00%)
summary +      4 in 00:00:02 =    2.2/s Avg:    85 Min:    49 Max:   184 Err:     0 (0.00%) Active: 0 Started: 50 Finished: 50
summary =    100 in 00:00:52 =    1.9/s Avg:   115 Min:    41 Max:   511 Err:     0 (0.00%)
Tidying up ...    @ May 20, 2026 12:45:02 AM CEST (1779230702752)
... end of run
Terminado: Test-Plan-50-users
Ejecutando: Test-Plan-80-users
Creating summariser <summary>
Created the tree successfully using /var/jenkins_home/workspace/pipeline-coffee-cart/performance/jmeter/test-plan/Test-Plan-80-users.jmx
Starting standalone test @ May 20, 2026 12:45:05 AM CEST (1779230705661)
Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
summary +     65 in 00:00:24 =    2.7/s Avg:   119 Min:    42 Max:   510 Err:     0 (0.00%) Active: 1 Started: 33 Finished: 32
summary +     80 in 00:00:30 =    2.7/s Avg:   124 Min:    41 Max:  1180 Err:     0 (0.00%) Active: 1 Started: 73 Finished: 72
summary =    145 in 00:00:54 =    2.7/s Avg:   121 Min:    41 Max:  1180 Err:     0 (0.00%)
summary +     15 in 00:00:05 =    2.8/s Avg:   107 Min:    42 Max:   193 Err:     0 (0.00%) Active: 0 Started: 80 Finished: 80
summary =    160 in 00:01:00 =    2.7/s Avg:   120 Min:    41 Max:  1180 Err:     0 (0.00%)
Tidying up ...    @ May 20, 2026 12:46:05 AM CEST (1779230765530)
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

#6 [cypress-tests 4/5] RUN npm ci
#6 CACHED

#7 [cypress-tests 2/5] WORKDIR /e2e
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
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
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
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Retrieved from Cache [10050] x 5 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/assets/index-b859522e.css (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/favicon.ico (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
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
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  | WARN-NEW: Cross-Origin-Embedder-Policy Header Missing or Invalid [90004] x 11 
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/sitemap.xml (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/ (200 OK)
[2Kzap-test-coffee-app  |       https://coffee-cart.app/?breakable=1 (200 OK)
[2Kzap-test-coffee-app  | FAIL-NEW: 0   FAIL-INPROG: 0  WARN-NEW: 12    WARN-INPROG: 0  INFO: 0 IGNORE: 0       PASS: 55
zap-test-coffee-app exited with code 0
Aborting on container exit...
 Container zap-test-coffee-app  Stopping
 Container zap-test-coffee-app  Stopped
[Pipeline] }
[Pipeline] // catchError
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (LocalStack)
[Pipeline] sh
+ docker compose -f cloud-testing/localstack/docker-compose.yml up -d
 Container localstack-coffee-shop  Creating
 Container localstack-coffee-shop  Created
 Container localstack-coffee-shop  Starting
 Container localstack-coffee-shop  Started
[Pipeline] sh
+ sleep 15
[Pipeline] sh
+ hostname
+ docker network connect localstack-network 181c4e6d445a
Error response from daemon: endpoint with name jenkins already exists in network localstack-network
+ true
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Cloud Setup)
[Pipeline] sh
+ apt-get install -y python3 python3-pip python3-venv zip
Reading package lists...
Building dependency tree...
Reading state information...
python3 is already the newest version (3.13.5-1).
python3-pip is already the newest version (25.1.1+dfsg-1).
python3-venv is already the newest version (3.13.5-1).
zip is already the newest version (3.0-15).
0 upgraded, 0 newly installed, 0 to remove and 21 not upgraded.
[Pipeline] sh
+ chmod +x cloud-testing/aws/scripts/setup_all.sh
[Pipeline] sh
+ docker inspect -f {{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}} localstack-coffee-shop
+ LOCALSTACK_IP=172.19.0.2
+ LOCALSTACK_URL=http://172.19.0.2:4566 bash cloud-testing/aws/scripts/setup_all.sh
========================================
  QA Cloud Setup — coffee-cart
========================================

Verificando LocalStack...
LocalStack disponible
Virtualenv activado
Instalando dependencias Python...

[1/4] Configurando S3...
Iniciando proceso: creación de bucket, subida y verificación del archivo...
Bucket "qa-s3-auto-bucket" creado exitosamente.
Archivo "auto-test.txt" subido exitosamente al bucket "qa-s3-auto-bucket".
Archivo "auto-test.txt" descargado correctamente y el contenido coincide.

[2/4] Configurando SQS...
==================================================
  SQS Setup — qa-failures
==================================================
Cola creada: "qa-failures-dlq-coffee-cart"
   URL: http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/qa-failures-dlq-coffee-cart
   ARN DLQ: arn:aws:sqs:us-east-1:000000000000:qa-failures-dlq-coffee-cart

Cola creada: "qa-failures-coffee-cart"
   URL: http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/qa-failures-coffee-cart

==================================================
  Cola principal : qa-failures-coffee-cart
  Dead Letter    : qa-failures-dlq-coffee-cart
==================================================

[3/4] Configurando DynamoDB...
==================================================
  DynamoDB Setup — qa_executions
==================================================
Tabla "qa_executions" creada exitosamente.
   Estado: ACTIVE
==================================================

[4/4] Deployando Lambda...
========================================
  Deploy Lambda: qa-validate-results
========================================
Empaquetando handler...
  adding: handler.py (deflated 67%)
function.zip generado
Deployando con Python/boto3...
Lambda creada
========================================
  Deploy finalizado: qa-validate-results
========================================

========================================
Setup completo

  Servicios disponibles en http://172.19.0.2:4566:
    S3        → qa-reports-coffee-cart
    S3        → qa-s3-auto-bucket
    SQS       → qa-failures-coffee-cart
    DynamoDB  → qa_executions
    Lambda    → qa-validate-results
========================================
[Pipeline] sh
+ apt-get install -y python3 python3-pip python3-venv zip awscli
Reading package lists...
Building dependency tree...
Reading state information...
python3 is already the newest version (3.13.5-1).
python3-pip is already the newest version (25.1.1+dfsg-1).
python3-venv is already the newest version (3.13.5-1).
zip is already the newest version (3.0-15).
awscli is already the newest version (2.23.6-1).
0 upgraded, 0 newly installed, 0 to remove and 21 not upgraded.
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] sh
+ docker inspect -f {{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}} localstack-coffee-shop
+ LOCALSTACK_IP=172.19.0.2
+ [ -n 172.19.0.2 ]
+ export LOCALSTACK_URL=http://172.19.0.2:4566
+ echo Usando LocalStack en: http://172.19.0.2:4566
Usando LocalStack en: http://172.19.0.2:4566
+ cloud-testing/venv/bin/python cloud-testing/aws/s3/upload_reports.py
=======================================================
  QA Reports Upload — coffee-cart
  Fecha: 2026-05-19
=======================================================
Bucket "qa-reports-coffee-cart" creado exitosamente.

Suite: CYPRESS (results-docker/cypress)
Directorio no encontrado: results-docker/cypress
   Subidos: 0 | Ignorados: 0

Suite: NEWMAN (results-docker/newman)
Subido: newman/2026-05-19/report.json
   Subidos: 1 | Ignorados: 1

Suite: JMETER (results-docker/jmeter)
Subido: jmeter/2026-05-19/Test-Plan-20-users.jtl
Subido: jmeter/2026-05-19/Test-Plan-100-users.jtl
Subido: jmeter/2026-05-19/Test-Plan-50-users.jtl
Subido: jmeter/2026-05-19/Test-Plan-80-users.jtl
   Subidos: 4 | Ignorados: 51

Suite: ZAP (results-docker/zap)
Subido: zap/2026-05-19/report.html
   Subidos: 1 | Ignorados: 1

=======================================================
  Total subidos : 6
  Total ignorados: 53

Contenido del bucket:
jmeter/2026-05-19/Test-Plan-100-users.jtl (22.2 KB)
jmeter/2026-05-19/Test-Plan-20-users.jtl (4.6 KB)
jmeter/2026-05-19/Test-Plan-50-users.jtl (11.2 KB)
jmeter/2026-05-19/Test-Plan-80-users.jtl (17.8 KB)
newman/2026-05-19/report.json (125.0 KB)
zap/2026-05-19/report.html (119.2 KB)
=======================================================
+ cloud-testing/venv/bin/python cloud-testing/aws/sqs/poll_failures.py
=======================================================
  SQS Poll — Revisando fallos del pipeline
=======================================================

=======================================================
Sin fallos en la cola — pipeline OK
=======================================================
[Pipeline] sh
+ docker compose -f cloud-testing/localstack/docker-compose.yml down
 Container localstack-coffee-shop  Stopping
 Container localstack-coffee-shop  Stopped
 Container localstack-coffee-shop  Removing
 Container localstack-coffee-shop  Removed
 Network localstack-network  Removing
 Network localstack-network  Resource is still in use
[Pipeline] sh
+ docker compose down --remove-orphans
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
