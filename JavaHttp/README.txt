[Build]
javac -classpath ./httpcomponents-client-4.3.3/lib/httpclient-4.3.3.jar:./httpcomponents-client-4.3.3/lib/httpcore-4.3.2.jar  JavaHttp.java

[Run]
java -classpath .:./httpcomponents-client-4.3.3/lib/httpclient-4.3.3.jar:./httpcomponents-client-4.3.3/lib/httpcore-4.3.2.jar:./httpcomponents-client-4.3.3/lib/commons-logging-1.1.3.jar JavaHttp https://tw.stock.yahoo.com/q/bc?s=2412
