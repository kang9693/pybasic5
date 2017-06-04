from setuptools import setup
import py2exe

# name, description, version등의 정보는 일반적인 setup.py와 같습니다.
setup(name="현금인출기 ",
      description="py2exe test application",
      version="0.0.1",
      options={"py2exe":
				{"includes":["lib"],
							#"lib.menu",
							
							#"lib.banner"],
							}},
	  
	  #windows=[{"script": "현금인출기.py"}],
	  console = ["현금인출기v0.1.py"],
      
      )