# HELLO


## INSTALL
'''
    pip install -r requirements.txt
'''

## INIT
'''
    dynaconf init -f toml
'''
⚙️  Configuring your Dynaconf environment
------------------------------------------
🐍 The file `config.py` was generated.

🎛️  settings.toml created to hold your settings.

🔑 .secrets.toml created to hold your secrets.

🙈 the .secrets.* is also included in `.gitignore`
  beware to not push your secrets to a public repo.

🎉 Dynaconf is configured! read more on https://dynaconf.com


## Override `port` from settings.toml
Optionally you can now use environment variables to override values per execution or per environment.

'''
  # override `port` from settings.toml file and automatically casts as `int` value.
  export DYNACONF_PORT=9900
'''
