python3 -m virtualenv env
cd env/Scripts
activate
cd ../../
pip3 install -r requirement.txt

uvicorn main:app --reload
uvicorn product.main:app --reload

pip3 install -r requirement.txt

openssl rand -hex 32
f2ab983bfbc98cc088cec549b61948064b2b2da66abb9912f1faf1ffeb131c6apython3 -m virtualenv env