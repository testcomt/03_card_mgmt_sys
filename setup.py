#! /usr/local/bin/python3

# if shebang not exist, when executing the setup.py in the terminal, error will be reported:
# taideMacBook-Air:05_deliver_card_mgmt taixiaomei$ ./setup.py build
# from: can't read /var/mail/distutils.core
# reason is:
# No, it's not the script, it's the fact that your script is not executed by Python at all.
# If your script is stored in a file named script.py, you have to execute it as python script.py,
# otherwise the default shell will execute it and it will bail out at the from keyword.
# (Incidentally, from is the name of a command line utility which prints names of those who have sent mail to the given username,
# so that's why it tries to access the mailboxes).

from distutils.core import setup

setup(name="card_mgmt",
      version=1.0,
      description="Manage Cards",
      long_description="Create/Modify/Query/Delete cards!",
      author="Tai Xiaomei",
      author_email="testcom@qq.com",
      url="www.sharetesting.com",
      py_modules=["card_mgmt.cards_main",
                  "card_mgmt.cards_tools",
                  "card_mgmt.cards_input_oo",
                  "card_mgmt.cards_input_non_oo"])

# 在执行install命令时出现如下错误：AttributeError: 'float' object has no attribute 'replace'
# 于是进入出错所在文件install_egg_info.py的68行，增加一行代码，version = str(version)
# 再次安装，即成功、

# taideMacBook-Air:card_mgmt-1.0 taixiaomei$ ls
# PKG-INFO  build     card_mgmt setup.py
# taideMacBook-Air:card_mgmt-1.0 taixiaomei$ python3 setup.py install
# running install
# running build
# running build_py
# running install_lib
# running install_egg_info
# Traceback (most recent call last):
# File "setup.py", line 25, in <module>
# "card_mgmt.cards_input_non_oo"])
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/core.py", line 148, in setup
# dist.run_commands()
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/dist.py", line 966, in run_commands
# self.run_command(cmd)
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/dist.py", line 985, in run_command
# cmd_obj.run()
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/command/install.py", line 557, in run
# self.run_command(cmd_name)
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/cmd.py", line 313, in run_command
# self.distribution.run_command(command)
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/dist.py", line 984, in run_command
# cmd_obj.ensure_finalized()
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/cmd.py", line 107, in ensure_finalized
# self.finalize_options()
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/command/install_egg_info.py", line 26, in finalize_options
# to_filename(safe_version(self.distribution.get_version())),
# File "/usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/command/install_egg_info.py", line 68, in safe_version
# version = version.replace(' ','.')
# AttributeError: 'float' object has no attribute 'replace'
# taideMacBook-Air:card_mgmt-1.0 taixiaomei$ vim /usr/local/Cellar/python/3.7.2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/command/install_egg_info.py
# taideMacBook-Air:card_mgmt-1.0 taixiaomei$ python3 setup.py install
# running install
# running build
# running build_py
# running install_lib
# running install_egg_info
# Writing /usr/local/lib/python3.7/site-packages/card_mgmt-1.0-py3.7.egg-info
# taideMacBook-Air:card_mgmt-1.0 taixiaomei$
