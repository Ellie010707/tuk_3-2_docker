mkdir kyl
cd kyl
git pull "https://github.com/Ellie010707/tuk_3-2_docker"
sudo apt-get install virtualenv
sudo apt-get install pip

virtualenv -p python3 venv
source venv/bin/activate

sudo apt-get install httpie 
http -v GET http://localhost:8081/api/start
