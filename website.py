import streamlit as st
import pandas as pd
import hashlib
from PIL import Image

from io import BytesIO
import requests

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjhdfDYTI3HNP0wpxBAp_YePhfyBj9GlLAmFgW2zUsTQiWJwkY_iUvVuhiT9AD2X81uJQalB89rYlw/pub?gid=2112212887&single=true&output=csv')
DB = r.content
df = pd.read_csv(BytesIO(DB), index_col=0)
df.columns = ['Curso', 'Nome', 'CPF', 'Endereco', 'Telefone', 'e-mail']
curso = df['Curso']
nome = df['Nome']
#mail = df['email'][[0]
#st.write(df)
#st.write(df['email'])

image = Image.open('desenvolvimento.jpg')
st.image(image, caption='Web site em desenvolvimento')
st.markdown(":books:")	
st.title("LINGUAGENS DE PROGRAMAÇÃO")
SUB_TITULO = '<p style="font-family:tahoma; color:Blue; font-size: 28px;">Desenvolvido pelo prof. Massaki de O. Igarashi</p>'
st.markdown(SUB_TITULO, unsafe_allow_html=True)

mystyle = '''
    <style>
        p {
            text-align: justify;
        }
    </style>
    '''
st.markdown(mystyle, unsafe_allow_html=True)
# Generate tree equal columns
#col1, col2, col3 = st.columns((1, 1, 1))
col1, col2 = st.columns((1,1))
with col1:
    st.info(
       """
    ### ***Atenção, principiante!***
    Para você que é leigo e está começando agora a programar, este material introdutório, uma espécie de **guia rápido**, está estruturado **com um passo-a-passo a ser seguido** com se fosse uma "receita de bolo". Então, por favor, siga um passo de cada vez e tome cuidado para o bolo não desandar!
    """    
    )
with col2:
    st.info(
    """
    ### ***Aprendizado colaborativo***
    Projetado para fornecer aos usuários um espaço sobre algumas Linguagens de Programação. O objetivo não é substituir o conteúdo institucional disponível para aulas, mas servir de suporte complementar ao aprendizado compartilhado. Espero que você faça bom uso!
    """
    )

st.markdown("""
#### ***Para referenciar este material:*** """)
st.warning("IGARASHI, Massaki de O. MICRO SITE SOBRE LINGUAGENS DE PROGRAMAÇÃO. Campinas - SP, 2022, v.1 01 de agosto de 2022. Disponível em: [link](endereço).")
    
task1 = st.selectbox("👈 Selecione a linguagem desejada:",
                    ["Linguagem de Programação C++", 
                     "Linguagem de Programação Pyhton",                                
                     "Linguagem de Programação R"                           
                     ])                                  

if task1 == "Linguagem de Programação C++": 

    SUB_TITULO1 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 01 - FERRAMENTAS NECESSÁRIAS</p>'
    st.markdown(SUB_TITULO1, unsafe_allow_html=True)

    cols = st.columns(1)
    cols[0].write('Antes de iniciar você precisa saber que precisará de um compilador; este compilador pode ser instalado no seu desktop, no seu celular ou simplesmente executado ambiente de núvem da internet (esta última opção pode ser executada de qualquer plataforma, basta acessar o navegador de internet do seu dispositivo).')
    st.markdown(
    """
    ###### Compiladores para S.O WINDOWS:
    - [Bloodshed Dev-C++](https://www.bloodshed.net/download.html)
    - [Code::Blocks](http://www.codeblocks.org/downloads/26)
    
    **OBSERVAÇÃO:** Instale a versão codeblocks-XX.XX ***mingw-setup.exe***. Pois ela inclui o compilador GCC/G++/GFortran e o GDB debugger necessários para a execução do seu programa 

    
    ###### Compiladores para S.O. ANDROID: 
    - [CppDroid](https://play.google.com/store/apps/details?id=name.antonsmirnov.android.cppdroid)
    - [CxxDroid](https://play.google.com/store/apps/details?id=ru.iiec.cxxdroid)
     
    ###### Compiladores WEB ONLINE:  
    - [Repl.it ](https://repl.it)
    - [OnlineGDBbeta](https://www.onlinegdb.com/online_c++_compiler)
    - [C++ Shell] (http://cpp.sh)
    - [myCompiler] (https://www.mycompiler.io/online-c++-compiler)
    - [Paiza.IO] (https://paiza.io/en/projects/new?language=cpp)
    - [CodeChef] (https://www.codechef.com/ide) 

   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    
    """
    )
    SUB_TITULO2 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 02: Estrutura básica de um programa C++</p>'
    st.markdown(SUB_TITULO2, unsafe_allow_html=True)
    
    cols = st.columns(1)
    cols[0].write('Ao ingressar no copilador, você precisa da estrutura básica, a seguir, para que seu programa seja executado:')
    
    coluna1, coluna2 = st.columns((1,1))
    with coluna1:
        st.info(
        """
        ###### include <iostream>
        ###### using namespace std;
        ###### int main()
        ###### {
        ######     return 0;
        ###### }
        """
        )
    with coluna2:
        st.info(
        """
        ***//Nosso 1º Programa é Hello prof. Massaki!***
        ###### include <iostream>
        ###### using namespace std;
        ###### int main()
        ###### {
        ######     cout<<"Hello prof. Massaki";
        ######     return 0;
        ###### }
        """
        )
    
    SUB_TITULO3 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 03: Explicações Básicas</p>'
    st.markdown(SUB_TITULO3, unsafe_allow_html=True)

    cols = st.columns(1)
    cols[0].write('Na verdade isto é um comando que informa que no resto do seu código o compilador deve considerar que você está usando o namespace padrão. Ou seja, serve para definir escopos para as estruturas do C++.')
    
    a1, a2 = st.columns((1,1))
    with a1:
        st.info(
        """
        ##### ***using namespace std;***
        Por exemplo, no caso de dois programadores em um mesmo projeto, digamos que cada um crie uma função void Funcao(void) que façam coisas absolutamente diferentes, uma forma de resolver esse conflito é usando um namespace diferente para cada programador.
        Se você não usasse esse using namespace std quase todas as funções ou classes da biblioteca padrão que você usasse você teria que colocar um std:: antes. ***Os dois comandos mais usados do C++ sem declarar using namespace std precisao da palavra std na frente:***
        ##### std::cout <<
        ##### std::cin>> 
        ##### Isso serve para te poupar de ficar digitando tanto!
        """
        )
    with a2:
        st.info(
        """
        ##### ***<iostream>***
        O cabeçalho padrão <iostream> declara objetos que controlam fluxos padrões de leitura e escrita de dados. Esse geralmente é o único cabeçalho você precisa incluir para executar entrada e saída de um programa C ++ console básico.
        ##### ***Alguns objetos dessa biblioteca são:***
        - cin, cout, cerr e clog
        - wcin, wcout, wcerr “wcerr”
        ##### ***<cstdlib>***
        Esta é uma das bibliotecas padrões do C++ que é responsável pelas seguintes funções úteis para conversão de string para ponto flutuante, sorteios numéricos, etc. 
        ##### ***Principais funções contidas nesta biblioteca:***
        - size_t; div_t; ldiv_t; abort; abs; atexit; atof; atoi; atol; bsearch; calloc; div; exit; free; getenv; labs; ldiv; malloc; mblen; mbstowcs; mbtowc; qsort; rand; realloc; srand; strtod; strtol; strtoul; system; wcstombs; wctomb;
        ##### ***<iomanip>***
        Esta biblioteca inclui vários manipuladores que permitem formar a escrita. 
        ##### ***Dentre eles merecem destaque:***
        - setw;
        - setfill;
        - e setprecision.
        """
        )
        
    SUB_TITULO4 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 04: Comentários no programa</p>'
    st.markdown(SUB_TITULO4, unsafe_allow_html=True)

    b1, b2 = st.columns((1,1))
    with b1:
        st.subheader("Numa única linha")
        st.info(
        """
        Os comentários de linha única começam com duas barras "//". 
        ***Exemplo:***
        ###### #include <iostream>
        ###### using namespace std;
        ###### int main()
        ###### {
        ######       //Este comentario nesta linha não executa!
        ######       cout << "Hello World!"; //Exibe Hello World na tela console
        ######       return 0;
        ###### }
        """
        )
    with b2:
        st.subheader("Em várias linhas")
        st.info(
        """
        Os comentários de várias linhas começam com " /* " e terminam com " */ ".
        ***Exemplo:*** 
        ######    /* Assim você pode inserir o enunciado 
        ######       ou explicação do funcionamento de um 
        ######       programa usanod várias linhas */
        ######
        ######       #include <iostream>
        ######       using namespace std;
        ######       int main()
        ###### {     cout << "Hello World!";  //Exibe Hello World na tela
        ######       return 0;
        ###### }
        """
        )
    
    SUB_TITULO5 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 05: Compilando um Hello World</p>'
    st.markdown(SUB_TITULO5, unsafe_allow_html=True)

    cols = st.columns(1)
    cols[0].write('O primeiro questionamento que se faz quando se tenta aprender uma linguagem de programação é por que o mundo inteiro faz como 1º programa (em qualquer linguagem de programação) a famosa exibição da palavra “Hello World”, que em português significa “Olá Mundo”. Não obstante, se você também quiser aprender qualquer coisa ligada ao mundo da eletrônica, precisa saber que todos mundo afora consideram como exemplo básico inicial exibir um “Hello  world”. Então aqui vão dois exemplos de programa C++ que exibem na tela do console “Hello World”.')


    d1, d2 = st.columns((1,1))
    with d1:
        st.info(
        """
        ***//Nosso 1º Programa é Hello Prof. Massaki!***
        ###### include <iostream>
        ###### 
        ###### int main()
        ###### {
        ######     **std::cout <<** "Hello Prof.Massaki!";
        ######     return 0;
        ###### }
        """
        )
    with d2:
        st.info(
        """
        ***//Nosso 1º Programa é Hello Prof. Massaki!***
        ###### include <iostream>
        ###### **using namespace std;**
        ###### int main()
        ###### {
        ######     **cout<<**"Hello Prof. Massaki";
        ######     return 0;
        ###### }
        """
        )
    
    st.title("Referências Bibliográficas")
    st.info(
    """
    **Bibliografia Básica**
    - PAMBOUKIAN, Sérgio V. D.; ZAMBONI, Lincoln C.; BARROS, Edson A. R. Aplicações Científicas em C++. 4. ed. São Paulo: Páginas & Letras, 2015. V1. 230 p.

    **Bibliografia Complementar**
    - CAPRON, Harriet L.; JOHNSON, J. A. Introdução à informática. 8. ed. São Paulo: Pearson/Prentice Hall, 2008. 

    - DEITEL, Harvey M.; DEITEL, Paul J. C++: como programar. 5. ed. São Paulo: Pearson Prentice Hall, 2008. 1163 p. 

    - HORSTMANN, Cay. Conceitos de computação com o essencial de C++. Tradução: Carlos A. L. Lisbôa e Maria Lúcia B. Lisbôa. Porto Alegre: Bookman Editora (Grupo A), 2005.p.36; p.157-199.Disponível em: < https://integrada.minhabiblioteca.com.br/#/books/9788577801770/pageid/155>

    - JOYANES AGUILAR, Luis. Programação em C++: algoritmos, estruturas de dados e objetos. 2. ed. São Paulo: McGraw-Hill, 2008. 768 p. 

    - MIZRAHI, Victorine Viviane. Treinamento em linguagem C++: módulo 1. 2. ed. São Paulo: Pearson Prentice Hall, 2009. 234 p. 

    - MIZRAHI, Victorine Viviane. Treinamento em linguagem C++: módulo 2. 2. ed. São Paulo: Pearson Prentice Hall, 2009. 309 p. 

    - SAVITCH, Walter J. C++ absoluto. São Paulo: Pearson/Addison Wesley, 2004. 612 p. 

    - STROUSTRUP, B. The C++ programming language. Special ed., 12th printing Boston: Addison-Wesley, 2005.

    """
    )    
# Security
#passlib,hashlib,bcrypt,scrypt

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():
	"""Simple Login App"""

	st.subheader("------ **Desenvolvido por: Massaki de O. Igarashi** -----")

	menu = ["Cursos",
            "Admin",
            "Contato",
            "SignUp"
            ]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Cursos":       
		st.subheader("ACESSO RESTRITO (em desenvolvimento): \n Preencha os dados abaixo:")
	elif choice == "Admin":
		st.subheader("Login Section")
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')        
		if st.sidebar.checkbox("Logar!"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
				task = st.selectbox("Task",["Add Post","PERFIL","Panorama_INSCRITOS"])
				if task == "Add Post":
					st.subheader("Add Your Post")
				elif task == "PERFIL":
					st.subheader("PERFIL DE USUÁRIO \n Linha 01 - Texto do perfil.")
				elif task == "Panorama_INSCRITOS":
					st.subheader(str(curso))                    
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					#st.dataframe(clean_db)                    
			else:
				st.warning("Incorrect Username/Password") 
	elif choice == "Contato":
		st.subheader("Massaki de O. Igarashi / e-mail: prof.massaki@gmail.com")
	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")


if __name__ == '__main__':
	main()
