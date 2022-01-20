import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()


setuptools.setup(
     name='dokr',  
     version='0.1',
     scripts=['dokr'] ,
     author="Deepak Kumar",
     author_email="deepak.kumar.iet@gmail.com",
     description="A Docker and AWS utility package",
     long_description=long_description,
   long_description_content_type="",
     url="https://github.com/hsudani/IOT",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
