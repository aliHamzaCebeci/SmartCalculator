lang = str(input("which language will you choose? türkçe or English"))
if lang not in ["türkçe","ingilizce","english","turkish","end"]:
    print("pls answer questions in correct way")

if lang == "türkçe":
    checkExit=input('hesap makinesinden çıkmak için "bitir" yazınız.')
    while checkExit != "bitir":
        try:
            try:
                want = (input("hangi işlemi yapmak istediğinizi yazınız. seçenekler: toplama, çıkarma, çarpma, bölme."))
                if want not in ["toplama","çıkarma","çarpma","bölme"]:
                    print("lütfen seçeneklerde olan işlemleri seçin")
                    continue
                num=int(input("ilk sayı nedir?"))
                num2=int(input("ikinci sayı nedir"))
            except ValueError:
                print("lütfen soruları doğru şekilde cevaplayınız")

            if want == "toplama" :
                print("cevap:",num+num2)
            elif want =="çıkarma" :
                 print("cevap:",num-num2)
            elif want == "bölme" :
                print("cevap:",num/num2)
            elif want == "çarpma":
                 print("cevap:",num*num2)
            checkExit = input('hesap makinesinden çıkmak için "bitir" yazınız.')
        except ValueError and ZeroDivisionError:
            print("lütfen soruları doğru şekilde cevaplayınız")

elif lang == "english":
    checkExitEng=input('please write "exit" if you want to finish the program')

    while checkExitEng != "exit":
        try:
            try:
                want1 = (input("which one do you want to do: addition, subtraction, multiplication, division."))

                if want1 not in ["addition", "subtraction", "multiplication", "division"]:
                    print("pls answer the questions in correct way")
                    continue
                num1 = int(input("what is first number?"))
                num3 = int(input("what is second number"))

            except ValueError:
                print("pls answer the questions in correct way")

            if want1 == "addition":
                print("aswer:",num1 + num3)
            elif want1 == "subtraction":
                print("answer:",num1 - num3)
            elif want1 == "multiplication":
                print("answer:",num1 * num3)
            elif want1 == "division":
                print("answer:",num1 / num3)
            checkExitEng = input('please write "exit" if you want to finish the program')

        except ValueError and ZeroDivisionError:
            print("pls answer the questions in correct way")
