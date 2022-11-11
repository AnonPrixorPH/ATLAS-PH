unzip methods.zip; unzip ATLAS-BYPASS.zip; unzip ATLAS-METHODS.zip; mv ATLAS-METHODS methods; mv ATLAS-BYPASS methods; chmod 777 methods/*
pip3 install -r requirements.txt
sudo apt -y install screen
python3 atlas.py
