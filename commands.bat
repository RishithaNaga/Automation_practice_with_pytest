selenium hub: java -jar selenium-server-<version>.jar hub

jenkins:java -jar jenkins.war

selenium node:java -jar selenium-server-<version>.jar node --detect-drivers true --hub http://localhost:4444

to generate logs: --log-cli-level=INFO --log-file=C:/Automation_practice_with_pytest/logs/log3.log --log-file-level=INFO --log-format="%(asctime)s [%(levelname)s] %(message)s" --log-date-format="%Y-%m-%d %H:%M:%S"
