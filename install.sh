unzip methods.zip; unzip ATLAS-METHODS.zip; chmod 777 methods/*
rm methods.zip ATLAS-METHODS.zip
pip3 install -r requirements.txt
sudo apt -y install screen
python3 atlas.py
