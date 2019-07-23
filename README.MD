##GEOHASH-NoSQL
A simple Implementation of the geohash library to encode and decode
latitudes and longitudes for easy storage.
The project also features implementing a dynamodb local instance and also on an amazon dynamodb-local docker image.
##REQUIREMENTS
Run pip3 install -r requirements.txt<br>
The original Geohash package can be installed using <br>
pip3 install geohash but the _____'_init___.py' has a slight flaw.
<br>One can either install the normal way and correct or install my forked repo where I have already effected the changes. <br>
The latter is used in the requirements file.<br>

##RUNNING DYNAMODB LOCALLY
To install a dynamodb instance to your local instance, follow the steps in the below link:<br>
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html <br>
Once downloaded and unzipped, navigate to the dynamodb folder by running <br>
cd dynamodb_local_latest<br>
To start the local dynamodb instance, assuming you have Java Runtime Environment (JRE) version 6.x or newer installed, run the command<br>
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb<br>
This fires up the local dynamoDB and thus, ready for use. Remember not to close this terminal instance.
