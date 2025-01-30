import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-akretion-profiloo",
    description="Meta package for akretion-profiloo Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-profile_mail',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
