echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
#python3.12 -m venv venv

# activate the virtual environment
#source venv/bin/activate
echo "python version"
echo python --version
# install all deps in the venv
pip install pipenv
pipenv shell
pipenv install
python manage.py makemigrations --noinput

python manage.py migrate --noinput
# collect static files using the Python interpreter from venv
python manage.py collectstatic --noinput

echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver