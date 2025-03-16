# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.youtube.com	TRUE	/	TRUE	1741772104	GPS	1
.youtube.com	TRUE	/	TRUE	1757576330	__Secure-ROLLOUT_TOKEN	CLmzzY_ZxMeHbxDB38yCmISMAxj25MyryouMAw%3D%3D
.youtube.com	TRUE	/	TRUE	1757576941	VISITOR_INFO1_LIVE	UE2PfnaEXYE
.youtube.com	TRUE	/	TRUE	1757576941	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgYg%3D%3D
.youtube.com	TRUE	/	TRUE	1776584942	PREF	tz=Asia.Kolkata
.youtube.com	TRUE	/	TRUE	1773306359	__Secure-1PSIDTS	sidts-CjEBEJ3XVx6Pj-eqPsJiGMe33KroM0t1Of1ZhXx1T6jO-QICZdynZ5vSt7ZUPhgiV7arEAA
.youtube.com	TRUE	/	TRUE	1773306359	__Secure-3PSIDTS	sidts-CjEBEJ3XVx6Pj-eqPsJiGMe33KroM0t1Of1ZhXx1T6jO-QICZdynZ5vSt7ZUPhgiV7arEAA
.youtube.com	TRUE	/	FALSE	1776330359	HSID	ArCjytIOpB_nkkVd9
.youtube.com	TRUE	/	TRUE	1776330359	SSID	AWcym7R9Y-AcWCsMG
.youtube.com	TRUE	/	FALSE	1776330359	APISID	WR70cHn-JCXGc09Q/AIBcXPWBbzdSfJ9s4
.youtube.com	TRUE	/	TRUE	1776330359	SAPISID	LM6JoEPlQJl3BlSp/Aq-jCGwbj4cwmPS9L
.youtube.com	TRUE	/	TRUE	1776330359	__Secure-1PAPISID	LM6JoEPlQJl3BlSp/Aq-jCGwbj4cwmPS9L
.youtube.com	TRUE	/	TRUE	1776330359	__Secure-3PAPISID	LM6JoEPlQJl3BlSp/Aq-jCGwbj4cwmPS9L
.youtube.com	TRUE	/	FALSE	1776330359	SID	g.a000ugjJFV2WHQ6g1ZrBp79ZL4qdGZ2jeIa8O3M77StAUnH6TpWa3QGbFSJ6561IhmgMKA0MWQACgYKAeQSAQASFQHGX2MiBtZ1WK575E8v8m7z2oVFDBoVAUF8yKoFyKJjAopRWp4_vHntOLW90076
.youtube.com	TRUE	/	TRUE	1776330359	__Secure-1PSID	g.a000ugjJFV2WHQ6g1ZrBp79ZL4qdGZ2jeIa8O3M77StAUnH6TpWaZswmmCYVteCfhguGKhzTiAACgYKAZESAQASFQHGX2MiK3n5eWyQNQ2pYVcBwxzcHhoVAUF8yKq7W3BTFSEisOw4OvmmbJh80076
.youtube.com	TRUE	/	TRUE	1776330359	__Secure-3PSID	g.a000ugjJFV2WHQ6g1ZrBp79ZL4qdGZ2jeIa8O3M77StAUnH6TpWaOlcIS2jlocwcYwMAuqi54gACgYKAZkSAQASFQHGX2MiMk6cu85xrFt22WiGohg7_RoVAUF8yKqQZpQU33E-dMqXixbshbIF0076
.youtube.com	TRUE	/	FALSE	1773561092	SIDCC	AKEyXzVN4YUJpjNtWmWENTmxbpoNMtIpD5n8RKNhLigDh50h-_oRJX80ReqWO_R5Z4wIbXpzpA
.youtube.com	TRUE	/	TRUE	1773561092	__Secure-1PSIDCC	AKEyXzVKgDugjHgaWUrXfdPpz_qqNtfh9G_7gt5ePX3zYIJwMI703VnXS--teleWUa3hEXLe
.youtube.com	TRUE	/	TRUE	1773561092	__Secure-3PSIDCC	AKEyXzWs1a2c7fVlfB-B1zJeL_QS059LNjZjx-TeMNeIIBmoh7Oi_nOI7_r4wNgbC5NbOYl8
.youtube.com	TRUE	/	TRUE	1776330360	LOGIN_INFO	AFmmF2swRAIgTeCJRZ1zOsD-8eZsbNkjaTLafIJ7-Yf9PPFjUzzciskCICnmngozXRzShA-huiHhtbeqmR9JfZK16YBnGfr43M_7:QUQ3MjNmeElFMUJSdENIM3F0emJUdUliOVZZWTI0WldneFpoT3dMcFlzbVN4TDl2c0l0OUxFeXZQMHg3X0lyNXBIZkMxR1FSS2lQZU55T1BkcUFMVThzbWdHTUFHZFo0dXdNcmk2YnQzTWNDa1dZVmFaX3VoeDVGWTJPVThTaXplQmwycVpNUmExTzlBT3RFT0FSYzNmYXhzQXZMbWhYNzVn
.youtube.com	TRUE	/	FALSE	1741770378	ST-19ov5as	csn=W68tC9Ltfxj9Pupj&itct=CI4BEIf2BBgAIhMI4YKnnZiEjAMVpXFeBB1iDjuJWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	FALSE	1741770388	ST-18jhcf3	csn=u2pEHreJGqK7vvoH&itct=CIIBEIf2BBgDIhMI4YKnnZiEjAMVpXFeBB1iDjuJWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	FALSE	1741770390	ST-cq6dvv	csn=u2pEHreJGqK7vvoH&itct=CFYQh_YEGAEiEwjhgqedmISMAxWlcV4EHWIOO4laD0ZFd2hhdF90b193YXRjaJoBBQgkEI4e
.youtube.com	TRUE	/	FALSE	1741770395	ST-1ulfwtt	csn=u2pEHreJGqK7vvoH&itct=CF8Q_FoiEwjhgqedmISMAxWlcV4EHWIOO4kyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
.youtube.com	TRUE	/	FALSE	1741770413	ST-13ou0e8	csn=kNtoHj_1LuXZrwzY&itct=CM0BEPxaGAAiEwjbq6CqmISMAxXEBYMDHeADGOsyB3JlbGF0ZWRInKKA5vH2yPJumgEFCAEQ-B0%3D
.youtube.com	TRUE	/	FALSE	1741933616	ST-16rsivp	csn=fuyGJ0RCR5rM_fR7&itct=CIsBEIf2BBgBIhMIrN-xqPiIjAMV1Z1LBR3q4ieYWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	FALSE	1741933693	ST-9q3c8l	csn=d5WtcRShlbRvFsh7&itct=CIcBEIf2BBgBIhMIh8PG0viIjAMV9phWAR0wMRpmWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	FALSE	1741957191	ST-bhldb0	csn=dW1S6nb0KXLodPph&itct=CI8BEIf2BBgAIhMI5v6ck9CJjAMVA1mdCR1oWTy9Wg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	FALSE	1741957228	ST-1la64oo	csn=cL-qN0LooUFAyyvF&itct=CIABEIf2BBgCIhMI_uyFptCJjAMVVC97Bx17-zTcWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	TRUE	0	YSC	5NYUCBpb1oY
.youtube.com	TRUE	/	FALSE	1742024957	ST-1fch2d8	csn=tCXTcpoib2UKzqeF&itct=CI4BEIf2BBgAIhMI8a70zsyLjAMV4YrYBR1-DyhhWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	TRUE	1742025641	CONSISTENCY	AKreu9u2Af_VL42TZePe0gJBNN27v4UYI8z9Faa4igR3A55JEuxu-BN9t-jqPCHZnXoFhOdcQOZH0JSdUx6Gz30w2Ot7cCOOPJztE4d6VWZxetCcO3TbmEKypWE
.youtube.com	TRUE	/	FALSE	1742025044	ST-ddb2f0	csn=jaO5uvlu4F6ofePq&itct=CIoBEIf2BBgBIhMIzqXF-syLjAMVFYnYBR1ptAjaWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	FALSE	1742025063	ST-8v9tx2	csn=zS5civkMzMRkk-9O&itct=CI4BEIf2BBgAIhMIzqXF-syLjAMVFYnYBR1ptAjaWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHg%3D%3D
.youtube.com	TRUE	/	FALSE	1742025066	ST-19zxdt	csn=zS5civkMzMRkk-9O&itct=CGYQ_FoiEwjOpcX6zIuMAxUVidgFHWm0CNoyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
"""

API_ID = os.getenv("API_ID", "28094744")
API_HASH = os.getenv("API_HASH", "a75af4285edc7747c57bb19147ca0b9b")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8084560097:AAEPifeVRNcag0XFm3YxuK_kOOiI7tOwHXk")
MONGO_URI = os.getenv("MONGO_DB", "mongodb+srv://tmglcd:kI1UijMr2jJXyOXY@cluster0.unjzi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5680454765").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", None)) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", None)) # optional with -100
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
