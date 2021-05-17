# cowin slots

```sh
python -m pip install --upgrade virtualenv
python -m virtualenv env
env/bin/python -m pip install --upgrade requests
# modify global script parameters if needed and execute it
env/bin/python cowin-slots.py
```

### NOTE
- Do not rely entirely on the script - it works today, may not work later
- Use your own bearer token (explained in the script)
- Check global variables to change the filters in script
- Limit the script execution to less than 20 times an hour