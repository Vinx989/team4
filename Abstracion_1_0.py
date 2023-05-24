"""
    Social Network Abstraction
    Questo programma rappresenta un social network dove è previsto la creazione di un account
    L'accesso al proprio account
    Pubblicare contenuti sottoforma di post  o rimuovere vecchi contenuti
    Commentare i post di altri utenti di Abstraction
    La possibilità di seguire le attività di altri utenti di Abstraction e di rimuoverli dalla lista dei seguiti

"""

users = [{'nome_user': 'Vinx989', 'nome':'vincenzo', 'cognome':'bruno', 'password':'trottola89!', 'posts':['Cosenza che bella giornata','La suppressata va senza finocchietto!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['pach90','Alerisp94','Ueloiol'], 'lista_commenti':[('pach90','che bello')]},
         {'nome_user': 'Alerisp94', 'nome':'alessandra', 'cognome':'rispoli', 'password':'rispoli94!', 'posts':['Torino che bella giornata','Universo sto arrivando!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['pach90','Vinx989','Ueloiol'], 'lista_commenti':[('Vinx989','che bello')]},
         {'nome_user': 'Pach90', 'nome':'nicola', 'cognome':'pacella', 'password':'nicolo90!', 'posts':['Firenze che bella giornata','La fiorentina batte il risotto alla milanese!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['Vinx989','Alerisp94','Ueloiol'], 'lista_commenti':[('Vinx989','che bello')]},
         {'nome_user': 'Ueloiol', 'nome':'stefano', 'cognome':'bassi', 'password':'bassi99!', 'posts':['Pavia che bella giornata','Noi fisici siamo degli eroi!!!','Il cielo è azzurro sopra berlino #campionidelMONDO'], 'amici':['pach90','Alerisp94','Vinx989'], 'lista_commenti':[('Vinx989','che bello')]}]


#in lista_utenti_oggetto ci sono gli oggetti utente
lista_utenti_oggetto = []


class Post:
    def __init__(self, username, contenuto):
        self.username = username
        self.post_stesso = contenuto
        self.lista_commenti_al_Post =[]

class Utente:

    # per istanziare gli oggetti Utente
    def __init__(self, username, nome, cognome, password):
        self.username = username
        self.nome = nome
        self.cognome = cognome
        self.password = password
        self.amici_utente = []
        self.homepage_utente = []
        lista_utenti_oggetto.append(self)
        # lista_utenti.append(self.username) #<---

    def indice_username(self,lista_utenti_oggetto):
        username_look = input('Quale amico vuoi cercare?\n')
        index = False
        for item in range(len(lista_utenti_oggetto)):
            if lista_utenti_oggetto[item].username == username_look:
                index = item
        return index

    # Per far accedere l'utente al Social Astraction
    def accedi(self, username, password):
        username_ins = input('inserisci username: ')
        password_ins = input('inserisci password: ')
        if username_ins == self.username and password_ins == self.password:
            return True
        else:
            return False

    def stampa_home(self):
        print(f'{self.username} home page!\n')
        for i in range(len(self.homepage_utente)):
            print(i, ':', self.homepage_utente[i])

    def stampa_amici(self):
        print(f'{self.username} amici!\n')
        for i in range(len(self.amici_utente)):
            print(i, ':', self.amici_utente[i])

    def crea_post(self):
        contenutoPost = input('Scrivi il tuo post: ')
        mio_post = Post(self.username, contenutoPost)
        self.homepage_utente.append(mio_post)
        self.stampa_home()

    # Cancelliamo un nostro post
    def cancella_post(self):
        if self.homepage_utente != []:
            self.stampa_home()
            index_to_pop = int(input('digita il numero del post da cancellare'))
            self.homepage_utente.pop(index_to_pop)
            print('Bravo, hai cancellato il tuo post!')

        else:
            print('Non hai post nella home!')

    # Inizia il follow di un Utente usando la lista lista_utente, che contiene le string con gli username degli Utenti
    def following(self, lista_utenti_oggetto=lista_utenti_oggetto):
        index = indice_username(lista_utenti_oggetto)
        #amico = input('inserisci il nome del tuo amico: ')
        if index != False:
            self.amici_utente.append(amico)
        else:
            print('questo utente non esiste')

    # Elimina follower poppa un amico dalla lista
    def un_following(self):
        try:
            for i in range(len(self.amici_utente)):
                print(i, ':', self.amici_utente[i])
            exAmico = input("Inserisci il nome dell'amico che vuoi bloccare con cattiveria: ")
            self.amici_utente.remove(exAmico)
        except:
            print("l'amico non c'è")

####################################################################################################

    def commenta_post(self):
        utenteX = input('Quale amico vuoi cercare?')
        index_amico = self.indice_username(lista_utenti_oggetto)
        for idx in range(len(lista_utenti_oggetto[index_amico].homepage_utente)):
            print(idx, ':', lista_utenti_oggetto[index_amico].homepage_utente[idx].post_stesso)
            for com in lista_utenti_oggetto[index_amico].homepage_utente[idx].lista_commenti_al_Post:
                print(com)
        try:
            index_post = int(input("Digita l'indice del post da commentare: "))
            commento = input('Inserisci il tuo commento al post: ')
            lista_utenti_oggetto[index_amico].homepage_utente[index_post].lista_commenti_al_Post.append((self.username, commento))
            print(lista_utenti_oggetto[index_amico].homepage_utente[index_post].post_stesso)
            for com in lista_utenti_oggetto[index_amico].homepage_utente[index_post].lista_commenti_al_Post:
                print(com, '\n')
        except:
            print('Qualcosa è andato storta. Riprova o contatta il servizio IT')

cont =0
for item in users:
    username = item['nome_user']
    nome = item['nome']
    cognome = item['cognome']
    password = item['password']
    lista_post = item['posts']
    lista_amici = item['amici']
    lista_commenti = item['lista_commenti']
    mario = Utente(username, nome, cognome, password)
    for item in lista_post:
        post_mario = Post(username,item)
        mario.homepage_utente.append(post_mario)
    for item in lista_commenti:
        mario.amici_utente.append(item)
    #lista_utenti_oggetto.append(mario)
    lista_utenti_oggetto[cont].stampa_home()
    lista_utenti_oggetto[cont].stampa_amici()
    cont += 1




def Registrazione():
    print('Inserisci il tuo Username, Nome, Cognome, Password')
    inRegistrazione = True

    while inRegistrazione:
        username = input('Inserisci il tuo Username: ')

        nomeTrovato = False
        for usr in lista_utenti_oggetto:
            if username == usr.username:
                nomeTrovato = True
                break

        if nomeTrovato == False:
            name = input('Inserisci il tuo Nome: ')
            surname = input('Inserisci il tuo Cognome: ')
            password = input('Inserisci il la tua Password: ')

            giacomino = Utente(username, name, surname, password)

            print(f'Grazie per la tua registrazione {username}, ora puoi accedere ad Abstraction!\n')
            inRegistrazione = False

        else:
            print("L'username o password già utilizzati. Vuoi riprovare?\n")
            continua = input('Premi Y per riprovare o qualsiasi tasto tornare indietro .\n')
            if continua.lower() != 'y':
                inRegistrazione = False



def Abstraction(NumeroUtente):
    print(f'Salve, numero utente {lista_utenti_oggetto[NumeroUtente].username}, scegli cosa vuoi fare')

    inAbstraction = True
    while inAbstraction:
        print('0. Per accedere con un altro account')
        print('1. Pubblica un Post')
        print('2. Cancella un Post')
        print('3. Commenta un Post')
        print('4. Aggiungi Amici')
        print('5. Rimuovi Amici\n')

        scelta = input('Scelta: ')

        if scelta == '0':
            print('grazie per esserti connesso. Arrivederci\n')
            inAbstraction = False
        elif scelta == '1':
            lista_utenti_oggetto[NumeroUtente].crea_post()
            # da sistemare in questo swich la scelta dell'utente a cui commentare i post
        elif scelta == '2':
            #input('Digita il nome di un utente')
            lista_utenti_oggetto[NumeroUtente].cancella_post()
        elif scelta == '3':
            #input('Digita il nome di un utente')
            lista_utenti_oggetto[NumeroUtente].commenta_post()
        elif scelta == '4':
            lista_utenti_oggetto[NumeroUtente].following()
        elif scelta == '4':
            lista_utenti_oggetto[NumeroUtente].un_following()
        else:
            print('inserisci scelta valida')
            pass


def AbstractionAccess():
    accesso_registrazione = True

    while accesso_registrazione:
        print('scegli se registrarti, accedere o uscire dal solcial Abstraction')
        print('0. Per Uscire')
        print('1. Per registrarti')
        print('2. Per accedere\n')

        scelta = input('Scelta: ')

        # Per uscire dal Primo Menu
        if scelta == '0':
            print('Arrivederci')
            accesso_registrazione = False

        # Per la registrazione, non si esce dal ciclo totale, si rimane dentro finchè non ti registri con un User assente
        elif scelta == '1':
            Registrazione()

        # accedere, poi dentro altro swithc InAbstract con le cose che si possono fare nel social
        elif scelta == '2':
            user_Ins = input('Inserisci il tuo Username: ')
            pass_Ins = input('Inserisci la tua Password: ')
            check_dat = False
            for idx in range(len(lista_utenti_oggetto)):
                if user_Ins == lista_utenti_oggetto[idx].username and pass_Ins == lista_utenti_oggetto[idx].password:
                    idx_Oggetto = idx
                    check_dat = True

            if check_dat == False:
                print('Username o password errata. Riprova\n')

            else:
                print("Accesso Eseguito!\n")
                Abstraction(idx_Oggetto)

        # else del menu principale, in caso è stata inserita una scelta a caso
        else:
            print('Inserisci scelta valida')


AbstractionAccess()
