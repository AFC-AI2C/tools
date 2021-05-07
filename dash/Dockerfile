FROM high101bro/python38-ai:latest

USER root

WORKDIR /opt/app-root
RUN mkdir /tmp/repo apps scripts default

# COPY *.whl /tmp/repo
# COPY *.tar.gz /tmp/repo

COPY scripts/app.py /opt/app-root/default/app.py 


RUN python3.8 -m pip install \
    dash                     \
    gunicorn

# cleanup downloaded packages
RUN rm -rf /opt/app-root/repo
# remove IB flagged 'secrets'
# RUN rm /opt/app-root/lib/python3.8/site-packages/future/backports/test/badcert.pem     \
#     /opt/app-root/lib/python3.8/site-packages/future/backports/test/badkey.pem         \
#     /opt/app-root/lib/python3.8/site-packages/future/backports/test/keycert2.pem       \
#     /opt/app-root/lib/python3.8/site-packages/future/backports/test/keycert.passwd.pem \
#     /opt/app-root/lib/python3.8/site-packages/future/backports/test/keycert.pem        \
#     /opt/app-root/lib/python3.8/site-packages/future/backports/test/ssl_key.passwd.pem \
#     /opt/app-root/lib/python3.8/site-packages/future/backports/test/ssl_key.pem

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN rm -rf /tmp/repo

HEALTHCHECK CMD curl --fail http://127.0.0.1:8050 || exit 1

# switch to default user to run the container
USER python3 

# port for default app.py
EXPOSE 8050

# the way to use this is to mount in an app.py to /opt/app-root/apps/app.py in the container
ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]

# Flask: 
# curl -O https://files.pythonhosted.org/packages/f2/28/2a03252dfb9ebf377f40fba6a7841b47083260bf8bd8e737b0c6952df83f/Flask-1.1.2-py2.py3-none-any.whl
# Flask-compress:
# curl -O https://files.pythonhosted.org/packages/b2/7a/9c4641f975fb9daaf945dc39da6a52fd5693ab3bbc2d53780eab3b5106f4/Flask_Compress-1.8.0-py3-none-any.whl
# plotly:
# curl -O https://files.pythonhosted.org/packages/1f/f6/bd3c17c8003b6641df1228e80e1acac97ed8402635e46c2571f8e1ef63af/plotly-4.14.3-py2.py3-none-any.whl
# dash_core:
# curl -O https://files.pythonhosted.org/packages/0f/ab/5ffeeed41117383d02485f5b9204dcfaa074bfbb3ff2559afac7b904ad5c/dash_core_components-1.14.1.tar.gz
# dash_render:
# curl -O https://files.pythonhosted.org/packages/72/fe/59a322edb128ad15205002c7b81e3f5e580f6791c4a100183289e05dbfcb/dash_renderer-1.8.3.tar.gz
# dash-html-components:
# curl -O https://files.pythonhosted.org/packages/02/ba/bb9427c62feb25bfbaf243894eeeb4e7c67a92b426ed0575a167100e436e/dash_html_components-1.1.1.tar.gz
# dash_core_components-1.14.1.tar.gz:
# curl -O https://files.pythonhosted.org/packages/0f/ab/5ffeeed41117383d02485f5b9204dcfaa074bfbb3ff2559afac7b904ad5c/dash_core_components-1.14.1.tar.gz
# dash-table:
# curl -O https://files.pythonhosted.org/packages/79/4b/de20584b7dc82dc6e572e8b596d21b1c6e39f13d19e8c9e6f1d67bed67fd/dash_table-4.11.1.tar.gz
# dash-1.18.1.tar.gz:
# curl -O https://files.pythonhosted.org/packages/dd/17/55244363969638edd1151de0ea4aa10e6a7849b42d7d0994e3082514e19d/dash-1.18.1.tar.gz
# future:
# curl -O https://files.pythonhosted.org/packages/45/0b/38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9/future-0.18.2.tar.gz
# Brotli:
# curl -O https://files.pythonhosted.org/packages/3a/7f/52adb1a253579749064d705f0b0db40adedc565b72eb22b68f1347db93cb/Brotli-1.0.9-cp27-cp27m-manylinux1_x86_64.whl
# pip-20.3.3-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/54/eb/4a3642e971f404d69d4f6fa3885559d67562801b99d7592487f1ecc4e017/pip-20.3.3-py2.py3-none-any.whl
# Jinja2-2.11.2-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/30/9e/f663a2aa66a09d838042ae1a2c5659828bb9b41ea3a6efa20a20fd92b121/Jinja2-2.11.2-py2.py3-none-any.whl
# MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl:
# curl -O https://files.pythonhosted.org/packages/b2/5f/23e0023be6bb885d00ffbefad2942bc51a620328ee910f64abe5a8d18dd1/MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl
# Werkzeug-1.0.1-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/cc/94/5f7079a0e00bd6863ef8f1da638721e9da21e5bacee597595b318f71d62e/Werkzeug-1.0.1-py2.py3-none-any.whl
# click-7.1.2-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl
# itsdangerous-1.1.0-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
# retrying-1.3.3.tar.gz:
# curl -O https://files.pythonhosted.org/packages/44/ef/beae4b4ef80902f22e3af073397f079c96969c69b2c7d52a57ea9ae61c9d/retrying-1.3.3.tar.gz
# six-1.15.0-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
# Pandas
# pandas-1.1.5-cp36-cp36m-manylinux1_x86_64.whl:
# curl -O https://files.pythonhosted.org/packages/c3/e2/00cacecafbab071c787019f00ad84ca3185952f6bb9bca9550ed83870d4d/pandas-1.1.5-cp36-cp36m-manylinux1_x86_64.whl
# numpy-1.19.5-cp36-cp36m-manylinux1_x86_64.whl:
# curl -O https://files.pythonhosted.org/packages/45/b2/6c7545bb7a38754d63048c7696804a0d947328125d81bf12beaa692c3ae3/numpy-1.19.5-cp36-cp36m-manylinux1_x86_64.whl
# python_dateutil-2.8.1-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl
# pytz-2020.5-py2.py3-none-any.whl:
# curl -O https://files.pythonhosted.org/packages/89/06/2c2d3034b4d6bf22f2a4ae546d16925898658a33b4400cfb7e2c1e2871a3/pytz-2020.5-py2.py3-none-any.whl
