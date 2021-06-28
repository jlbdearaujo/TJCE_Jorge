import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Jorge159=pd.read_csv('CLAUDIO159.csv.zip',sep=';')
Jorge436=pd.read_csv('CLAUDIO436.csv.zip',sep=';')
Jorge1116=pd.read_csv('CLAUDIO1116.csv.zip',sep=';')

CLAU436=pd.read_csv('DD436.csv',sep=';')
CLAU436.rename({'HERE':'MOVIMENTAÇÃO','QUANTIDADE':'POWER'},axis=1,inplace=True)
TIPOMV436=list(Jorge436.DETIPOMVPROCESSO.value_counts(ascending=False).index)
TIPOMV436.insert(0,'NONE')

CLAU159=pd.read_csv('DD159.csv',sep=';')
CLAU159.rename({'HERE':'MOVIMENTAÇÃO','QUANTIDADE':'POWER'},axis=1,inplace=True)
TIPOMV159=list(Jorge159.DETIPOMVPROCESSO.value_counts(ascending=False).index)
TIPOMV159.insert(0,'NONE')

CLAU1116=pd.read_csv('DD1116.csv',sep=';')
CLAU1116.rename({'HERE':'MOVIMENTAÇÃO','QUANTIDADE':'POWER'},axis=1,inplace=True)
TIPOMV1116=list(Jorge1116.DETIPOMVPROCESSO.value_counts(ascending=False).index)
TIPOMV1116.insert(0,'NONE')


st.sidebar.title('UNIFOR - DADOS ESTRUTURADOS')
st.sidebar.write('Jorge Luiz')
listaclasse=['Execução de Título Extrajudicial','Execução Fiscal','Procedimento do Juizado Especial Cível']
paginaseleciona=st.sidebar.selectbox('Selecione uma Classe',listaclasse)

if paginaseleciona=='Execução de Título Extrajudicial':
	st.title(paginaseleciona)
	selemv=st.selectbox('Selecione a movimentação de Origem',TIPOMV159)
	if selemv!='NONE':
		fig, ax = plt.subplots(figsize=(5,3.5))
		ax.tick_params(axis="x", labelsize=20)
		ax.tick_params(axis="y", labelsize=20)
		ax.set_xlabel(r'$\Delta T$',fontsize=20)
		ax.set_xlim(0,Jorge159[Jorge159['ORIGEM']==selemv]['DTIN'].max())
		ax.set_title(selemv,fontsize=20)
		ax.hist(Jorge159[Jorge159['ORIGEM']==selemv]['DTIN'],bins=60,color='orange',alpha=1.0)
		st.pyplot(fig)
		laux=CLAU159[CLAU159['ORIGEM']==selemv].sort_values('POWER',ascending=False)[['MOVIMENTAÇÃO','POWER']].reset_index().drop('index',axis=1).copy()
		laux['POWER']=(laux['POWER']-laux['POWER'].min())/(laux['POWER'].max()-laux['POWER'].min())
		st.write('Tempo médio',Jorge159[Jorge159['ORIGEM']==selemv]['DTIN'].mean())
		
		st.write('As maiores relações são:',laux)
		
		laux2=list(laux['MOVIMENTAÇÃO'].values.copy())
		laux2.insert(0,'NONE')
		selemv2=st.selectbox('Escolha a movimentação futura',laux2)
		if selemv2!='NONE':
			fig2, ax1 = plt.subplots(figsize=(5,3.5))
			ax1.tick_params(axis="x", labelsize=20)
			ax1.tick_params(axis="y", labelsize=20)
			ax1.set_xlabel(r'$\Delta T$',fontsize=20)
			tmedio=Jorge159[Jorge159['ORIGEM']==selemv2]['DTIN'].mean()
			ax1.set_xlim(0,Jorge159[Jorge159['ORIGEM']==selemv2]['DTIN'].max())
			ax1.set_title(selemv2,fontsize=20)
			ax1.hist(Jorge159[Jorge159['ORIGEM']==selemv2]['DTIN'],bins=20,color='green',alpha=0.50)
			st.pyplot(fig2)
			st.write('Tempo médio',tmedio)

		
if paginaseleciona=='Execução Fiscal':
	st.title(paginaseleciona)
	selemv=st.selectbox('Selecione a movimentação de Origem',TIPOMV1116)
	if selemv!='NONE':
		fig, ax = plt.subplots(figsize=(5,3.5))
		ax.tick_params(axis="x", labelsize=20)
		ax.tick_params(axis="y", labelsize=20)
		ax.set_xlabel(r'$\Delta T$',fontsize=20)
		ax.set_xlim(0,Jorge1116[Jorge1116['ORIGEM']==selemv]['DTIN'].max())
		ax.set_title(selemv,fontsize=20)
		ax.hist(Jorge1116[Jorge1116['ORIGEM']==selemv]['DTIN'],bins=60,color='orange',alpha=1.0)
		st.pyplot(fig)
		laux=CLAU1116[CLAU1116['ORIGEM']==selemv].sort_values('POWER',ascending=False)[['MOVIMENTAÇÃO','POWER']].reset_index().drop('index',axis=1).copy()
		st.write('Tempo médio',Jorge1116[Jorge1116['ORIGEM']==selemv]['DTIN'].mean())
		laux['POWER']=(laux['POWER']-laux['POWER'].min())/(laux['POWER'].max()-laux['POWER'].min())
		st.write('As maiores relações são:',laux)
		laux2=list(laux['MOVIMENTAÇÃO'].values.copy())
		laux2.insert(0,'NONE')
		selemv2=st.selectbox('Escolha a movimentação futura',laux2)
		if selemv2!='NONE':
			fig, ax = plt.subplots(figsize=(5,3.5))
			ax.tick_params(axis="x", labelsize=20)
			ax.tick_params(axis="y", labelsize=20)
			ax.set_xlabel(r'$\Delta T$',fontsize=20)
			tmedio=Jorge1116[Jorge1116['ORIGEM']==selemv2]['DTIN'].mean()
			ax.set_xlim(0,Jorge1116[Jorge1116['ORIGEM']==selemv2]['DTIN'].max())
			ax.set_title(selemv2,fontsize=20)
			ax.hist(Jorge1116[Jorge1116['ORIGEM']==selemv2]['DTIN'],bins=20,color='green',alpha=1.0)
			st.pyplot(fig)
			st.write('Tempo médio',tmedio)
			
if paginaseleciona=='Procedimento do Juizado Especial Cível':
	st.title(paginaseleciona)
	selemv=st.selectbox('Selecione a movimentação de Origem',TIPOMV436)
	if selemv!='NONE':
		fig, ax = plt.subplots(figsize=(5,3.5))
		ax.tick_params(axis="x", labelsize=20)
		ax.tick_params(axis="y", labelsize=20)
		ax.set_xlabel(r'$\Delta T$',fontsize=20)
		ax.set_xlim(0,Jorge436[Jorge436['ORIGEM']==selemv]['DTIN'].max())
		ax.set_title(selemv,fontsize=20)
		ax.hist(Jorge436[Jorge436['ORIGEM']==selemv]['DTIN'],bins=60,color='orange',alpha=1.0)
		st.pyplot(fig)
		st.write('Tempo médio',Jorge436[Jorge436['ORIGEM']==selemv]['DTIN'].mean())
		laux=CLAU436[CLAU436['ORIGEM']==selemv].sort_values('POWER',ascending=False)[['MOVIMENTAÇÃO','POWER']].reset_index().drop('index',axis=1).copy()

		laux['POWER']=(laux['POWER']-laux['POWER'].min())/(laux['POWER'].max()-laux['POWER'].min())
		st.write('As maiores relações são:',laux)
		laux2=list(laux['MOVIMENTAÇÃO'].values.copy())
		laux2.insert(0,'NONE')
		selemv2=st.selectbox('Escolha a movimentação futura',laux2)
		if selemv2!='NONE':
			fig, ax = plt.subplots(figsize=(5,3.5))
			ax.tick_params(axis="x", labelsize=20)
			ax.tick_params(axis="y", labelsize=20)
			ax.set_xlabel(r'$\Delta T$',fontsize=20)
			tmedio=Jorge436[Jorge436['ORIGEM']==selemv2]['DTIN'].mean()
			ax.set_xlim(0,Jorge436[Jorge436['ORIGEM']==selemv2]['DTIN'].max())
			ax.set_title(selemv2,fontsize=20)
			ax.hist(Jorge436[Jorge436['ORIGEM']==selemv2]['DTIN'],bins=20,color='green',alpha=1.0)
			st.pyplot(fig,tmedio)
			st.write('Tempo médio',Jorge1116[Jorge1116['ORIGEM']==selemv2]['DTIN'].mean())
