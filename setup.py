from setuptools import setup

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()
    AUTHOR_NAME='NAND KISHOR KUMAR'
    SRC_REPO='src'
    LIST_OF_REQUIREMENTS=['streamlit']
    
    
    setup(
        name='SRC_REPO',
        version='0.0.1',
        author=AUTHOR_NAME,
        author_emal='999nandkishor@gmail,com',
        description='A streamlit app for demo',
        package=[SRC_REPO],
        install_requires=LIST_OF_REQUIREMENTS,
    )
    