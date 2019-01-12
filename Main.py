def intro():
    # Prints out the main menu for the bank account application form.

        print('\n***************************************************')
        print('*                                                 *')
        print('*    Welcome to loyds Bank account application!   *')
        print('*                                                 *')
        print('*    1. Sole application                          *')
        print('*    2. Joint application                         *')
        print('*    3. Quit                                      *')
        print('*                                                 *')
        print('***************************************************')

def quit_program():
    # Code to terminate the program.

    print('Thanks for visiting us today! Have a great day!')
    quit()

intro()

while True: #keeps the program running until user types quit
    answer = input('\nWhat would you like to do today?')

    if answer == '1':
        def section3_info():  # prints ALL the info on section 3

            print('How we process your personal information\n\n'
                  'Who looks after your personal information:\nYour personal information will be held by Lloyds Bank Plc which is '
                  'part of the Lloyds Banking Group. More information on the Group can be found at www.lloydsbankinggroup.com\n\n'
                  'How we use your personal information\n\nWe will use your personal information:\n\n -To provide products and '
                  'services, manage your relationship with us and comply with any laws or regulations we are subject to (for '
                  'example the laws \nthat prevent financial crime or the regulatory requirements governing the products we '
                  'offer).\n -Other purposes including improving our services, exercising our rights in relation to agreements and '
                  'contracts and identifying products and services that may be of interest\n\nTo support us with the above we '
                  'analyse information we know about you and how you use our products and services, including some automated '
                  'decision making. \nYou can find out more about how we do this, and in what circumstances you can ask us to stop, '
                  'in our full privacy notice.\n\nWho we share your personal information with\n\nYour personal information will be '
                  'shared within Lloyds Banking Group and other companies that provide services to you or us, \nso that we and any '
                  'other companies in our Group can look after your relationship with us. \nBy sharing this information it enables '
                  'us to better understand our customers’ needs, run accounts and policies, and provide products and services '
                  'efficiently. \nThis processing may include activities which take place outside of the European Economic Area. '
                  '\nIf this is the case we will ensure appropriate safeguards are in place to protect your personal information. '
                  '\nYou can find out more about how we share your personal information with credit reference agencies below and '
                  'can access more information about how else we share your information in our full privacy notice.')

            print(
                'Where we collect your personal information from\n\nWe will collect personal information about you from a number '
                'of sources including:\n\n -Information given to us on application forms, when you talk to us in branch, over the '
                'phone or through the device you use and when new services are requested.\n -From analysis of how you operate our '
                'products and services, including the frequency, nature, location, origin and recipients of any payments\n -From '
                'or through other organisations (for example card associations, credit reference agencies, insurance companies, '
                'retailers, comparison websites, social media and fraud prevention agencies).\n -In certain circumstances '
                'we may also use information about health or criminal convictions but we will only do this where allowed by '
                'law or if you give us your consent.\n\nYou can find out more about where we collect personal information '
                'about you from in our full privacy notice.\n\nDo you have to give us your personal information\n\nWe may be '
                'required by law, or as a consequence of any contractual relationship we have, to collect certain personal '
                'information. \nFailure to provide this information may prevent or delay us fulfilling these obligations '
                'or performing services\n\nWhat rights you have over your personal information\n\nThe law gives you a number '
                'of rights in relation to your personal information including:\n\n -the right to access the personal information '
                'we have about you. This includes information from application forms, statements, correspondence '
                'and call recordings.\n -Thee right to get us to correct personal information that is wrong or incomplete.\n -In '
                'certain circumstances, the right to ask us to stop using or delete your personal information.\n -From 25 May '
                '2018 you will have the right to receive any personal information we have collected from you in an \n easily '
                're-usable format when it’s processed on certain grounds, such as consent or for contractual reasons. \n You '
                'can also ask us to pass this information on to another organisation.\n\nYou can find out more about these rights '
                'and how you can exercise them in our full privacy notice.\n\nOther Individuals you have financial links with\n\n'
                'We may also collect personal information about other individuals who you have a financial link with. \n'
                'This may include people who you have joint accounts or policies with such as your partner/spouse, dependents, '
                'beneficiaries or \npeople you have commercial links to, for example other directors or officers of your company.')

            print(
                '\nWe will collect this information to assess any applications, provide the services requested and to carry '
                'out credit reference and fraud prevention checks. \nYou can find out more about how we process personal '
                'information about individuals with whom you have a financial link in our full privacy notice\n\n'
                'How we use credit reference agencies\n\nIn order to process your application we may supply your personal '
                'information to credit reference agencies (CRAs) including how you use our \nproducts and '
                'services and they will give us information about you, such as about your financial history. '
                '\nWe do this to assess creditworthiness and product suitability, check your identity, '
                'manage your account, trace and recover debts and prevent criminal activity.\n\nWe may also continue to exchange '
                'information about you with CRAs on an ongoing basis, including about your settled accounts and '
                'any debts not fully repaid on time, \ninformation on funds going into the account, the balance on '
                'the account and, if you borrow, details of your repayments or whether you repay in full and on '
                'time. \nCRAs will share your information with other organisations, for example other organisations '
                'you ask to provide you with products and services. \nYour data will also be linked to the data of '
                'any joint applicants or other financial associates as explained above.\n\nYou can find out more about the '
                'identities of the CRAs, and the ways in which they use and share personal information, in our full '
                'privacy notice.\n\nHow we use fraud prevention agencies\n\nThe personal information we have collected from '
                'you and anyone you have a financial link with may be shared with fraud prevention agencies \nwho will use it '
                'to prevent fraud and money laundering and to verify your identity. If fraud is detected, you could be '
                'refused certain services, finance or employment. \nFurther details of how your information will be '
                'used by us and these fraud prevention agencies, and your data protection rights, can be found in '
                'our full privacy notice.')


        def section3_info2():

            print(
                'Our full privacy notice\n\nIt is important that you understand how the personal information you give us will '
                'be used. \nTherefore, we strongly advise that you read our full privacy notice, which you can find at '
                'http://www.lloydsbank.com/privacy.asp or you can ask us for a copy.\n\nHow you can contact us\n\nIf you have '
                'any questions or require more information about how we use your personal '
                'information please contact us using https://secure.lloydsbank.com/retail/contact_us/how-we-can-help.asp. '
                '\nYou can also call us on 0345 602 1997.\n\nIf you feel we have not answered your question Lloyds '
                'Banking Group has a Group Data Privacy Officer, who you can contact on 0345 602 1997 and tell us '
                'you want to speak to our Data Privacy Officer.\n\nVersion Control\n\nThis notice was last updated '
                'in February 2018')


        solecustomer_account_usage = input('\nYour information will now be store in a file.'
                                           '\nYou can also type quit to end the application form at anytime.'
                                           '\n\nWhat will you be using the Account for?')
        if solecustomer_account_usage.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            solecustomer_existing_question = input('\nAre you an exisiting Lloids Bank customer?\n\n1. Yes \n2. No\n')

            if solecustomer_existing_question == '1' or solecustomer_existing_question == 'Yes':
                solecustomer_existing = 'Yes'
                break
            elif solecustomer_existing_question == '2' or solecustomer_existing_question == 'No':
                solecustomer_existing = 'No'
                break
            elif solecustomer_existing_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        while True:  # Loops the question
            solecustomer_title_question = input(
                '\nWhat is your title ?\n\n1. Mr.\n2. Mrs. \n3. Miss. \n4. Ms. \n\nIf other, please specify\n')

            if solecustomer_title_question == '1' or solecustomer_title_question == 'Mr.':
                solecustomer_title = 'Mr.'
                break
            elif solecustomer_title_question == '2' or solecustomer_title_question == 'Mrs.':
                solecustomer_title = 'Mrs.'
                break
            elif solecustomer_title_question == '3' or solecustomer_title_question == 'Miss.':
                solecustomer_title = 'Miss.'
                break
            elif solecustomer_title_question == '4' or solecustomer_title_question == 'Ms.':
                solecustomer_title = 'Ms.'
                break
            elif solecustomer_title_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer_title = solecustomer_title_question
                break

        solecustomer_lastname = input('\nWhat is your last name ?\n')
        if solecustomer_lastname.lower() == 'quit':
            quit_program()
        solecustomer_firstname = input('\nWhat is your first name ?\n')
        if solecustomer_firstname.lower() == 'quit':
            quit_program()

        print('\nPleasure to have you here today', solecustomer_title, solecustomer_lastname, solecustomer_firstname,
              '\nLet us continue with the application\n')  # printing title and name out to the applicant.

        while True:  # Loops the question
            solecustomer_othername_question = input(
                '\nAny other name you use/have used in the past?\n\n1. Yes \n2. No\n')

            if solecustomer_othername_question == '1' or solecustomer_othername_question == 'Yes':
                solecustomer_othername = input('Please specify.')
                break
            elif solecustomer_othername_question == '2' or solecustomer_othername_question == 'No':
                solecustomer_othername = 'No'
                break
            elif solecustomer_othername_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_dob = input('\nWhat is your date of birth?\n\nPlease format it like DDMMYY'
                                 '\nFor example 01 01 90 for being born 1st of Jan in 1990\n')
        if solecustomer_dob.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            solecustomer_gender_question = input(
                '\nWhat is your gender ?\n\nMale \nFemale \n\nIf other, please specify\n')

            if solecustomer_gender_question == '1' or solecustomer_gender_question == 'Male':
                solecustomer_gender = 'Male'
                break
            elif solecustomer_gender_question == '2' or solecustomer_gender_question == 'Female':
                solecustomer_gender = 'Female'
                break
            elif solecustomer_gender_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer_gender = solecustomer_gender_question
                break

        student_question = input('\nIf you are a student, you will only need to complete this '
                                 'form if you do not meet the criteria for a Student account'
                                 '\nType quit to terminate the process now or anything else to continue')
        if student_question.lower() == 'quit':
            quit_program()
        else:
            print('Lets continue\n')

        solecustomer_occupation = 'No'
        solecustomer_unemployed = 'N/A'

        while True:  # Loops the question
            solecustomer_occupation_question = input(
                '\nWhat is your occupation right now?\n\n1. Employed \n2. Self employed \n3. Part time \n'
                '4. Unemployed \n5. Not working \n6. Seeking work \n7. Retired \n8. Student'
                ' \n\nIf other, please specify\n')

            if solecustomer_occupation_question == '1' or solecustomer_occupation_question == 'Employed':
                solecustomer_occupation = 'Employed'
                break
            elif solecustomer_occupation_question == '2' or solecustomer_occupation_question == 'Self employed':
                solecustomer_occupation = 'Self employed'
                break
            elif solecustomer_occupation_question == '3' or solecustomer_occupation_question == 'Part time':
                solecustomer_occupation = 'Part time'
                break
            elif solecustomer_occupation_question == '4' or solecustomer_occupation_question == 'Unemployed':
                solecustomer_occupation = 'Unemployed'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '5' or solecustomer_occupation_question == 'Not working':
                solecustomer_occupation = 'Not working'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '6' or solecustomer_occupation_question == 'Seeking work':
                solecustomer_occupation = 'Seeking work'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '7' or solecustomer_occupation_question == 'Retired':
                solecustomer_occupation = 'Retired'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '8' or solecustomer_occupation_question == 'Student':
                solecustomer_occupation = 'Student'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break

            elif solecustomer_occupation_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer_occupation_question = solecustomer_occupation_question
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break

        solecustomer_cob = input('\nYour country of birth ?\n')
        if solecustomer_cob.lower() == 'quit':
            quit_program()

        solecustomer_tob = input('\nYour Town/City of birth ?\n')
        if solecustomer_tob.lower() == 'quit':
            quit_program()

        solecustomer_nationality = input('\nWhat is your nationality ?\n')
        if solecustomer_nationality.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            solecustomer_addionalnationality_question = input(
                '\nDo you have any addional nationalities ?\n\n1. Yes\n2. No\n')

            if solecustomer_addionalnationality_question == '1' or solecustomer_addionalnationality_question == 'Yes':
                solecustomer_addionalnationality = input('Please specify.\n')
                break
            elif solecustomer_addionalnationality_question == '2' or solecustomer_addionalnationality_question == 'No':
                solecustomer_addionalnationality = 'No'
                break
            elif solecustomer_addionalnationality_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_countryofresidence = input('\nWhat is your country of residence ?\n')
        if solecustomer_nationality.lower() == 'quit':
            quit_program()

        solecustomer_taxresident = input(
            '\nWhich countries are you tax resident in ?\nPlease note: This is the country where '
            'an individual is resident under the tax laws of such jurisdiction\n')
        if solecustomer_taxresident.lower() == 'quit':
            quit_program()

        # First page done.

        solecustomer_tin = input('\nIf you have a Taxpayer Identification Number (TIN) for '
                                 'other countries, please provide details.\nGuidance: By TIN we mean, '
                                 'Taxpayer Identification number, or similar Tax payer reference number '
                                 'you hold for country(ies) you are tax resident in\n')
        if solecustomer_tin.lower() == 'quit':
            quit_program()

        # Defaulting the numbers to nothing until the user type something.
        solecustomer_telephonenumber_home = 'N/A'
        solecustomer_telephonenumber_mobile = 'N/A'
        solecustomer_telephonenumber_work = 'N/A'

        while True:  # Loops the question
            solecustomer_telephonenumber_question = input(
                '\nYour telephone numbers and area dialing codes ?\n\n1. Home\n2. Mobile\n3. Work')

            if solecustomer_telephonenumber_question == '1' or solecustomer_telephonenumber_question == 'Home':
                solecustomer_telephonenumber_home = input('Please specify.')
                solecustomer_telephonenumber_home_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer_telephonenumber_home_question.lower() == 'no' \
                        or solecustomer_telephonenumber_home_question == '2':
                    break

            elif solecustomer_telephonenumber_question == '2' or solecustomer_telephonenumber_question == 'Mobile':
                solecustomer_telephonenumber_mobile = input('Please specify.')
                solecustomer_telephonenumber_mobile_question = input('Would you like to fill in any other '
                                                                     'numbers?\n\n1. Yes\n2. No')
                if solecustomer_telephonenumber_mobile_question.lower() == 'no' \
                        or solecustomer_telephonenumber_mobile_question == '2':
                    break

            elif solecustomer_telephonenumber_question == '3' or solecustomer_telephonenumber_question == 'Work':
                solecustomer_telephonenumber_work = input('Please specify.')
                solecustomer_telephonenumber_work_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer_telephonenumber_work_question.lower() == 'no' \
                        or solecustomer_telephonenumber_work_question == '2':
                    break

            elif solecustomer_telephonenumber_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_residentalhomeaddress = input('\nYour home address (where you live)\n')
        if solecustomer_residentalhomeaddress.lower() == 'quit':
            quit_program()

        solecustomer_residentalpostcode = input('\nPostcode:\n')
        if solecustomer_residentalpostcode.lower() == 'quit':
            quit_program()

        solecustomer_residentalcountry = input('\nCountry:\n')
        if solecustomer_residentalcountry.lower() == 'quit':
            quit_program()

        solecustomer_residentaldate = input(
            '\When did you start living at this address ?\n\nPlease format it like MMYYYY'
            '\nFor example 011993 for starting living there January 1993\n')
        if solecustomer_residentaldate.lower() == 'quit':
            quit_program()

        # Setting to N/A in case user types No.
        solecustomer_previousresidentalhomeadress = 'N/A'
        solecustomer_previousresidentalpostcode = 'N/A'
        solecustomer_previousresidentalcountry = 'N/A'

        while True:  # Loops the question
            solecustomer_previousresidental_question = input(
                '\nHave you lived there less than three years ?\n\n1. Yes\n2. No\n')

            if solecustomer_previousresidental_question == '1' or solecustomer_previousresidental_question == 'Yes':
                solecustomer_previousresidentalhomeadress = input('\nYour previous address (where you lived)\n')
                if solecustomer_previousresidentalhomeadress.lower() == 'quit':
                    quit_program()
                solecustomer_previousresidentalpostcode = input('\nPostcode:\n')
                if solecustomer_previousresidentalpostcode.lower() == 'quit':
                    quit_program()
                solecustomer_previousresidentalcountry = input('\nCountry:\n')
                if solecustomer_previousresidentalcountry.lower() == 'quit':
                    quit_program()
                break
            elif solecustomer_previousresidental_question == '2' or solecustomer_previousresidental_question == 'No':
                solecustomer_previousresidental = 'No'
                break
            elif solecustomer_previousresidental_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again\n')

        # Sets them to N/A in case the user type No.
        solecustomer_correspondencehomeaddress = 'N/A'
        solecustomer_correspondencepostcode = 'N/A'
        solecustomer_correspondencecountry = 'N/A'
        solecustomer_correspondencresidental = 'N/A'

        while True:  # Loops the question
            solecustomer_correspondenceadress_question = input(
                '\nIs your correspondence address different from your current home address ?\n\n1. Yes\n2. No\n')

            if solecustomer_correspondenceadress_question == '1' or solecustomer_correspondenceadress_question == 'Yes':
                solecustomer_correspondencehomeaddress = input('\nYour correspondence address\n')
                if solecustomer_correspondencehomeaddress.lower() == 'quit':
                    quit_program()
                solecustomer_correspondencepostcode = input('\nPostcode:\n')
                if solecustomer_correspondencepostcode.lower() == 'quit':
                    quit_program()
                    solecustomer_correspondencecountry = input('\nCountry:\n')
                if solecustomer_correspondencecountry.lower() == 'quit':
                    quit_program()
                break
            elif solecustomer_correspondenceadress_question == '2' or solecustomer_correspondenceadress_question == 'No':
                solecustomer_correspondencresidental = 'No'
                break
            elif solecustomer_correspondenceadress_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again\n')

        solecustomer_debitcard = 'Yes'  # Defaulting to Yes

        # Defaulting to N/A in case user says no.
        solecustomer_newdebitcardname = 'N/A'
        solecustomer_newdebitcardmpn = 'N/A'
        solecustomer_newdebitcarddob = 'N/A'

        while True:  # Loops the question
            solecustomer_debitcard_question = input(
                '\nWould you like to apply for a debit card ?\n\n1. Yes\n2. No\n')

            if solecustomer_debitcard_question == '1' or solecustomer_debitcard_question == 'Yes':
                solecustomer_newdebitcard_question = input('\nAre you a new debit card customer ?\n\n1. Yes\n2. No\n')
                if solecustomer_newdebitcard_question == '1' or solecustomer_newdebitcard_question == 'Yes':
                    solecustomer_newdebitcardname = input('\nCustomer name to appear on card: \n')
                    if solecustomer_newdebitcardname.lower() == 'quit':
                        quit_program()
                    solecustomer_newdebitcardmpn = input('\nMothers previous name ? \n')
                    if solecustomer_newdebitcardmpn.lower() == 'quit':
                        quit_program()
                    solecustomer_newdebitcarddob = input('\nYour date of birth ?\n\nPlease format it like DDMMYY'
                                                         '\nFor example 010193 means you were born 1st of January in 1993\n')
                    if solecustomer_newdebitcarddob.lower() == 'quit':
                        quit_program()
                    break
                if solecustomer_newdebitcard_question == '2' or solecustomer_newdebitcard_question == 'No':
                    solecustomer_newdebitcardname = input('\nCustomer name to appear on card: \n')
                    if solecustomer_newdebitcardname.lower() == 'quit':
                        quit_program()
                    solecustomer_newdebitcarddob = input('\nYour date of birth ?\n\nPlease format it like DDMMYY'
                                                         '\nFor example 010193 means you were born 1st of January in 1993\n')
                    if solecustomer_newdebitcarddob.lower() == 'quit':
                        quit_program()
                    break
            elif solecustomer_debitcard_question == '2' or solecustomer_debitcard_question == 'No':
                solecustomer_debitcard = 'No'
                break
            elif solecustomer_debitcard_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        section3_info()

        while True:  # Loops the question
            solecustomer_section3_question = input(
                '\n\n\nPlase read about how we process your personal information above.\n Do you agree? '
                '(Typing 2, no or quit will terminate your application)\n\n1. Yes\n2. No')

            if solecustomer_section3_question == '1' or solecustomer_section3_question.lower() == 'yes':
                break
            elif solecustomer_section3_question == '2' or solecustomer_section3_question.lower() == 'no':
                quit_program()
            elif solecustomer_section3_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Defaults answers to no
        solecustomer_marketing_internetbanking = 'No'
        solecustomer_marketing_email = 'No'
        solecustomer_marketing_post = 'No'
        solecustomer_marketing_devicemessaging = 'No'
        solecustomer_marketing_textmessages = 'No'
        solecustomer_marketing_phone = 'No'
        solecustomer_marketing_none = 'Yes'

        print('\nYour marketing choices\n\nWe would like to keep you up to date on products and offers that may '
              'be of interest to you. Please select how you would like to hear from us below. \nThese choices won’t affect '
              'any necessary information we need to send you such as statements and, don’t worry, you can change your mind '
              'and update your preferences at any time.')

        while True:  # Loops the question
            solecustomer_marketing_question = input(
                '\nAre you interested in any of these options ?\nType "done" or 8 when you are done selecting the ones '
                'you want.\n\n1. Internet Banking \n-You’ll see relevant messages when you log on to Internet Banking and our '
                'apps. If you do not pick this, you may still see messages, but they won’t be tailored to you.\n2. Em'
                'ail\n3. Post\n4. Device Messaging\n-You’ll receive relevant notifications to your mobile device\n5. Text messages\n6. Phone\n7. None'
                '\n8. Done\n\nBy saying yes you are giving consent for Lloyds Bank to use your personal information to send '
                'you relevant offers and products. \nLloyds Bank includes the following legal entities: Lloyds Bank plc; Lloyds '
                'Bank Insurance Services Ltd; and Halifax Share Dealing Limited.\n\nOccasionally we will send you selected '
                'offers from other companies within Lloyds Banking Group that may be relevant to you.')

            if solecustomer_marketing_question == '1':
                solecustomer_marketing_internetbanking = 'Yes'
            elif solecustomer_marketing_question == '2':
                solecustomer_marketing_email = 'Yes'
            elif solecustomer_marketing_question == '3':
                solecustomer_marketing_post = 'Yes'
            elif solecustomer_marketing_question == '4':
                solecustomer_marketing_devicemessaging = 'Yes'
            elif solecustomer_marketing_question == '5':
                solecustomer_marketing_textmessages = 'Yes'
            elif solecustomer_marketing_question == '6':
                solecustomer_marketing_phone = 'Yes'
            elif solecustomer_marketing_question == '7':
                solecustomer_marketing_none = 'None wanted'
                break
            elif solecustomer_marketing_question == '8' or solecustomer_marketing_question.lower() == 'done':
                break
            elif solecustomer_marketing_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        section3_info2()

        while True:  # Loops the question
            solecustomer_section3_question = input(
                '\n\n\nPlase read about how we process your personal information above.\n Do you agree? '
                '(Typing 2, no or quit will terminate your application)\n\n1. Yes\n2. No')

            if solecustomer_section3_question == '1' or solecustomer_section3_question.lower() == 'yes':
                break
            elif solecustomer_section3_question == '2' or solecustomer_section3_question.lower() == 'no':
                quit_program()
            elif solecustomer_section3_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')


        def quit_program():
            # Code to terminate the program.

            print('Thanks for visiting us today! Have a great day!')
            quit()


        solecustomer_workingoccupation = 'N/A'
        solecustomer_workingemployersname = 'N/A'
        solecustomer_workingemployersaddress = 'N/A'
        solecustomer_workingemployerspostcode = 'N/A'
        solecustomer_workingcurrentemployer = 'N/A'
        solecustomer_workingemploymentpensionable = 'N/A'

        while True:  # Loops the question
            solecustomer_working_question = input(
                '\nAre you currently working ?\n\n1. Yes \n2. No\n')

            if solecustomer_working_question == '1' or solecustomer_working_question == 'Yes':
                solecustomer_working = 'Yes'
                solecustomer_workingoccupation = input('What is your occupation ?')
                if solecustomer_workingoccupation.lower() == 'quit':
                    quit_program()
                solecustomer_workingemployersname = input('What is your employers name ?')
                if solecustomer_workingemployersname.lower() == 'quit':
                    quit_program()
                solecustomer_workingemployersaddress = input('What is your employers address ?')
                if solecustomer_workingemployersaddress.lower() == 'quit':
                    quit_program()
                solecustomer_workingemployerspostcode = input(
                    'What is the postcode (If known, type na if not available)')
                if solecustomer_workingemployerspostcode.lower() == 'quit':
                    quit_program()
                solecustomer_workingcurrentemployer = input('\nHow long have you worked for you curent empl'
                                                            'oyer ?\n\nPlease format it like YYMM'
                                                            '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer_workingcurrentemployer.lower() == 'quit':
                    quit_program()
                solecustomer_workingpreviousemployer = input('\nHow long did you work for your previous empl'
                                                             'oyer ?\n\nPlease format it like YYMM'
                                                             '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer_workingpreviousemployer.lower() == 'quit':
                    quit_program()
                solecustomer_workingemploymentpensionable_question = input(
                    'Is your employment pensionable ?\n\n1. Yes \n2. No\n')
                if solecustomer_workingemploymentpensionable_question == '1' or solecustomer_workingemploymentpensionable_question == 'Yes':
                    solecustomer_workingemploymentpensionable = 'Yes'
                    break
                elif solecustomer_workingemploymentpensionable_question == '2' or solecustomer_workingemploymentpensionable_question == 'No':
                    solecustomer_workingemploymentpensionable = 'No'
                    break
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_working_question == '2' or solecustomer_working_question == 'No':
                solecustomer_working = 'No'
                solecustomer_workingpreviousemployer = input('\nHow long did you work for your previous empl'
                                                             'oyer ?\n\nPlease format it like YYMM'
                                                             '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer_workingpreviousemployer.lower() == 'quit':
                    quit_program()
                    break
                break

        # Predefine some answers unless changed.
        solecustomer_income_salaryfrequency = 'N/A'
        solecustomer_income_salary = 'N/A'
        solecustomer_income_benefitsfrequency = 'N/A'
        solecustomer_income_benefits = 'N/A'
        solecustomer_income_pensionfrequency = 'N/A'
        solecustomer_income_pension = 'N/A'
        solecustomer_income_investmentsfrequency = 'N/A'
        solecustomer_income_investments = 'N/A'
        solecustomer_income_othersfrequency = 'N/A'
        solecustomer_income_othersspecify = 'N/A'
        solecustomer_income_others = 'N/A'

        print('Income:')

        while True:  # Loops the question
            solecustomer_income_question = input(
                '\nIs any of the following source of your income ?\n\n1. Salary/wages\n2. Benefits\n3. Pension\n4. Inve'
                'stments\n5. Others')

            if solecustomer_income_question == '1' or solecustomer_income_question == 'Salary/wages':
                solecustomer_income_salaryfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_salarysource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_salarysource == '1':
                    solecustomer_income_salary = 'Direct to a bank'
                elif solecustomer_income_salarysource == '2':
                    solecustomer_income_salary = 'Cheque'
                elif solecustomer_income_salarysource == '3':
                    solecustomer_income_salary = 'Cash'
                elif solecustomer_income_salarysource == '4':
                    solecustomer_income_salary = 'Into this account'
                elif solecustomer_income_salarysource.lower() == 'quit':
                    quit_program()
                solecustomer_income_salarysource_question = input('Would you like to fill in any other '
                                                                  'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_salarysource_question.lower() == 'no' \
                        or solecustomer_income_salarysource_question == '2':
                    break
                elif solecustomer_income_salarysource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '2' or solecustomer_income_question == 'Benefits':
                solecustomer_income_benefitsfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_benefitssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_benefitssource == '1':
                    solecustomer_income_benefits = 'Direct to a bank'
                elif solecustomer_income_benefitssource == '2':
                    solecustomer_income_benefits = 'Cheque'
                elif solecustomer_income_benefitssource == '3':
                    solecustomer_income_benefits = 'Cash'
                elif solecustomer_income_benefitssource == '4':
                    solecustomer_income_benefits = 'Into this account'
                elif solecustomer_income_benefitssource.lower() == 'quit':
                    quit_program()
                solecustomer_income_benefitssource_question = input('Would you like to fill in any other '
                                                                    'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_benefitssource_question.lower() == 'no' \
                        or solecustomer_income_benefitssource_question == '2':
                    break
                elif solecustomer_income_benefitssource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '3' or solecustomer_income_question == 'Pension':
                solecustomer_income_pensionfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_pensionsource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_pensionsource == '1':
                    solecustomer_income_pension = 'Direct to a bank'
                elif solecustomer_income_pensionsource == '2':
                    solecustomer_income_pension = 'Cheque'
                elif solecustomer_income_pensionsource == '3':
                    solecustomer_income_pension = 'Cash'
                elif solecustomer_income_pensionsource == '4':
                    solecustomer_income_pension = 'Into this account'
                elif solecustomer_income_pensionsource.lower() == 'quit':
                    quit_program()
                solecustomer_income_pensionsource_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_pensionsource_question.lower() == 'no' \
                        or solecustomer_income_pensionsource_question == '2':
                    break
                elif solecustomer_income_pensionsource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '4' or solecustomer_income_question == 'Investments':
                solecustomer_income_investmentsfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_investmentssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_investmentssource == '1':
                    solecustomer_income_investments = 'Direct to a bank'
                elif solecustomer_income_investmentssource == '2':
                    solecustomer_income_investments = 'Cheque'
                elif solecustomer_income_investmentssource == '3':
                    solecustomer_income_investments = 'Cash'
                elif solecustomer_income_investmentssource == '4':
                    solecustomer_income_investments = 'Into this account'
                elif solecustomer_income_investmentssource.lower() == 'quit':
                    quit_program()
                solecustomer_income_investmentssource_question = input('Would you like to fill in any other '
                                                                       'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_investmentssource_question.lower() == 'no' \
                        or solecustomer_income_investmentssource_question == '2':
                    break
                elif solecustomer_income_investmentssource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '5' or solecustomer_income_question == 'Others':
                solecustomer_income_othersspecify = input('Please state type of income.')
                solecustomer_income_othersfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_otherssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_otherssource == '1':
                    solecustomer_income_others = 'Direct to a bank'
                elif solecustomer_income_otherssource == '2':
                    solecustomer_income_others = 'Cheque'
                elif solecustomer_income_otherssource == '3':
                    solecustomer_income_others = 'Cash'
                elif solecustomer_income_otherssource == '4':
                    solecustomer_income_others = 'Into this account'
                elif solecustomer_income_otherssource.lower() == 'quit':
                    quit_program()
                solecustomer_income_otherssource_question = input('Would you like to fill in any other '
                                                                  'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_otherssource_question.lower() == 'no' \
                        or solecustomer_income_otherssource_question == '2':
                    break
                elif solecustomer_income_otherssource_question.lower() == 'quit':
                    quit_program()

        solecustomer_income_monthly = input('How much is your total net monthly income?')
        solecustomer_income_monthlyaccount = input('How much are expected through this account per month ?')

        solecustomer_commitments_mortgage = input('\nWhat is your monthly commitments to Mortgage/rent ?\n')
        if solecustomer_commitments_mortgage.lower() == 'quit':
            quit_program()

        solecustomer_commitments_loans = input('\nWhat is your monthly commitments to HP/other loans ?\n')
        if solecustomer_commitments_loans.lower() == 'quit':
            quit_program()

        solecustomer_commitments_lloaydsbankloans = input(
            '\nWhat is your monthly commitments to Lloads Bank loans ?:\n')
        if solecustomer_commitments_lloaydsbankloans.lower() == 'quit':
            quit_program()

        solecustomer_commitments_total = input('\nWhat is your monthly commitments overall ?:\n')
        if solecustomer_commitments_total.lower() == 'quit':
            quit_program()

        # Predefining some answers.
        solecustomer_nosavings = 'No'
        solecustomer_llbsavings = 'No'
        solecustomer_llbnlbbsavings = 'No'
        solecustomer_nlbbsavings = 'No'

        print('Savings:')

        while True:  # Loops the question
            solecustomer_savings_question = input(
                '\nWhat type of savings do you have ?\n\n1. No savings\n2. Lloyds Bank savings only\n3. LLoyds Bank and '
                'non-Lloyds Bank savings\n4. Non-Lloyds Bank savings only')

            if solecustomer_savings_question == '1':
                solecustomer_nosavings = 'Yes'
                solecustomer_nosavings_question = input('\nWould you like to fill in any other '
                                                        'numbers?\n\n1. Yes\n2. No')
                if solecustomer_nosavings_question.lower() == 'no' \
                        or solecustomer_nosavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_nosavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer_savings_question == '2':
                solecustomer_llbsavings = 'Yes'
                solecustomer_llbsavings_question = input('\nWould you like to fill in any other '
                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer_llbsavings_question.lower() == 'no' \
                        or solecustomer_llbsavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_llbsavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer_savings_question == '3':
                solecustomer_llbnlbbsavings = 'Yes'
                solecustomer_llbnlbbsavings_question = input('\nWould you like to fill in any other '
                                                             'numbers?\n\n1. Yes\n2. No')
                if solecustomer_llbnlbbsavings_question.lower() == 'no' \
                        or solecustomer_llbnlbbsavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_llbnlbbsavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer_savings_question == '4':
                solecustomer_nlbbsavings = 'Yes'
                solecustomer_nlbbsavings_question = input('\nWould you like to fill in any other '
                                                          'numbers?\n\n1. Yes\n2. No')
                if solecustomer_nlbbsavings_question.lower() == 'no' \
                        or solecustomer_nlbbsavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_nlbbsavings_question.lower() == 'quit':
                    quit_program()

        while True:  # Loops the question
            solecustomer_bankingdetails_question = input(
                'Is this a personal or business account?\n\n1. Personal\n2. Business\n')
            if solecustomer_bankingdetails_question == '1' or solecustomer_bankingdetails_question == 'Personal':
                solecustomer_bankingdetails = 'Personal'
                break
            elif solecustomer_bankingdetails_question == '2' or solecustomer_bankingdetails_question == 'Business':
                solecustomer_bankingdetails = 'Business'
                break
            elif solecustomer_bankingdetails_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Fixing potention answers.
        solecustomer_facilitiesclosedwhy = 'N/A'

        print('Other banking details:')

        while True:  # Loops the question
            solecustomer_facilities_question = input('\nWhich of the following facilitie'
                                                     's do you use: \n\n1. Cheque card\n2. Debit card\n')

            if solecustomer_facilities_question == '1' or solecustomer_facilities_question == 'Cheque card':
                solecustomer_facilities = 'Cheque card'
                solecustomer_facilitiestime = input(
                    '\nHow long have you banked there ?\n\nPlease format it like YYMM\nFor example 03 05 for be'
                    'ing born three years and five months\n')
                if solecustomer_facilitiestime.lower() == 'quit':
                    quit_program()
                solecustomer_facilitiesclosed_question = input('Is the account to be closed ?\n\n1. Yes\n2. No')
                if solecustomer_facilitiesclosed_question == '1' or solecustomer_facilitiesclosed_question == 'Yes':
                    solecustomer_facilitiesclosed = 'Yes'
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                        break
                elif solecustomer_facilitiesclosed_question == '2' or solecustomer_facilitiesclosed_question == 'No':
                    solecustomer_facilitiesclosed = 'No'
                    solecustomer_facilitiesclosedwhy = input('Please explain why\n')
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                        break
                    if solecustomer_facilitiestransfer_question == '2' or solecustomer_facilitiestransfer_question == 'No':
                        solecustomer_facilitiestransfer = 'No'
                        break
                elif solecustomer_facilitiesclosed_question.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_facilities_question == '2' or solecustomer_facilities_question == 'Debit card':
                solecustomer_facilities = 'Cheque card'
                solecustomer_facilitiestime = input(
                    '\nHow long have you banked there ?\n\nPlease format it like YYMM\nFor example 03 05 for be'
                    'ing born three years and five months\n')
                if solecustomer_facilitiestime.lower() == 'quit':
                    quit_program()
                solecustomer_facilitiesclosed_question = input('Is the account to be closed ?\n\n1. Yes\n2. No')
                if solecustomer_facilitiesclosed_question == '1' or solecustomer_facilitiesclosed_question == 'Yes':
                    solecustomer_facilitiesclosed = 'Yes'
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                elif solecustomer_facilitiesclosed_question == '2' or solecustomer_facilitiesclosed_question == 'No':
                    solecustomer_facilitiesclosed = 'No'
                    solecustomer_facilitiesclosedwhy = input('Please explain why\n')
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                        break
                    if solecustomer_facilitiestransfer_question == '2' or solecustomer_facilitiestransfer_question == 'No':
                        solecustomer_facilitiestransfer = 'No'
                        break
                elif solecustomer_facilitiesclosed_question.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            elif solecustomer_facilities_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Predetermining some answers.
        solecustomer_creditcard_total = 'N/A'
        solecustomer_creditcard_limit = 'N/A'
        solecustomer_creditcard_lloyds = 'No'
        solecustomer_creditcard_otherchargecard = 'No'
        solecustomer_creditcard_otherstorecard = 'No'
        solecustomer_creditcard_otherother = 'No'
        solecustomer_creditcard_otherotherspecify = 'N/A'

        print('Your credit card detail:')

        while True:  # Loops the question
            solecustomer_creditcard_question = input('\nDo you hold a credit card? \n\n1. Yes\n2. No\n')

            if solecustomer_creditcard_question == '1' or solecustomer_creditcard_question == 'Yes':
                solecustomer_creditcard = 'Yes'
                solecustomer_creditcard_total = input('\nHow many do you have ? ')
                if solecustomer_creditcard_total.lower() == 'quit':
                    quit_program()
                solecustomer_creditcard_lloyds_question = input('\nAre any lloyds Bank ? \n\n1. Yes\n2. No\n')
                if solecustomer_creditcard_lloyds_question.lower() == 'quit':
                    quit_program()
                if solecustomer_creditcard_lloyds_question == '1' or solecustomer_creditcard_lloyds_question == 'Yes':
                    solecustomer_creditcard_lloyds = 'Yes'
                    solecustomer_creditcard_limit = input('What is your credit limit ?')
                    if solecustomer_creditcard_limit.lower() == 'quit':
                        quit_program()
                    break
                else:
                    break
            if solecustomer_creditcard_question == '2' or solecustomer_creditcard_question == 'No':
                solecustomer_creditcard = 'No'
                solecustomer_creditcard_lloyds_question = input('\nAre any lloyds Bank ? \n\n1. Yes\n2. No\n')
                if solecustomer_creditcard_lloyds_question.lower() == 'quit':
                    quit_program()
                if solecustomer_creditcard_lloyds_question == '1' or solecustomer_creditcard_lloyds_question == 'Yes':
                    solecustomer_creditcard_lloyds = 'Yes'
                    solecustomer_creditcard_limit = input('What is your credit limit ?')
                    if solecustomer_creditcard_limit.lower() == 'quit':
                        quit_program()
                    break
                else:
                    break
            else:
                print('\nInvalid entry, try again')

        while True:
            solecustomer_creditcard_other = input(
                'What other card type(s) do you hold ? \n\n1. Chargecard\n2. Storecard\n3. Other\n4. None')
            if solecustomer_creditcard_other == '1' or solecustomer_creditcard_other == 'Chargecard':
                solecustomer_creditcard_otherchargecard = 'Yes'
                solecustomer_creditcard_otherchargecard_question = input('\nWould you like to fill in any other '
                                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer_creditcard_otherchargecard_question == '2' or solecustomer_creditcard_otherchargecard_question == 'No':
                    break
            if solecustomer_creditcard_other == '2' or solecustomer_creditcard_other == 'Storecard':
                solecustomer_creditcard_otherstorecard = 'Yes'
                solecustomer_creditcard_otherstorecard_question = input('\nWould you like to fill in any other '
                                                                        'numbers?\n\n1. Yes\n2. No')
                if solecustomer_creditcard_otherstorecard_question == '2' or solecustomer_creditcard_otherstorecard_question == 'No':
                    break
            if solecustomer_creditcard_other == '3' or solecustomer_creditcard_other == 'Other':
                solecustomer_creditcard_otherother = 'Yes'
                solecustomer_creditcard_otherotherspecify = input('Please specify')
                solecustomer_creditcard_otherchargecard_question = input('\nWould you like to fill in any other '
                                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer_creditcard_otherchargecard_question == '2' or solecustomer_creditcard_otherchargecard_question == 'No':
                    break
            if solecustomer_creditcard_other == '4' or solecustomer_creditcard_other == 'None':
                break
            else:
                print('\nInvalid entry, try again')

        # Predetermining answer.
        solecustomer_mortgage_lloyds = 'No'

        print('Mortage details:')

        while True:  # Loops the question
            solecustomer_mortgage_question = input('\nDo you have a mortgage ?\n\n1. Yes\n2. No\n')

            if solecustomer_mortgage_question == '1' or solecustomer_mortgage_question == 'Yes':
                solecustomer_mortgage = 'Yes'
                solecustomer_mortgage_lloyds_question = input('\nIs it with Lloyds Bank ?\n\n1. Yes\n2. No\n')
                if solecustomer_mortgage_lloyds_question == '1' or solecustomer_mortgage_lloyds_question == 'Yes':
                    solecustomer_mortgage_lloyds = 'Yes'
                    break
                elif solecustomer_mortgage_lloyds_question.lower() == 'quit':
                    quit_program()
                else:
                    break
            if solecustomer_mortgage_question == '2' or solecustomer_mortgage_question == 'No':
                solecustomer_mortgage = 'No'
                break
            elif solecustomer_mortgage_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_mortgage_balance = input('\nWhat is the outstanding balance on your mortgage?:\n')
        if solecustomer_mortgage_balance.lower() == 'quit':
            quit_program()

        solecustomer_mortgage_value = input('\nWhat is the value of your house?:\n')
        if solecustomer_mortgage_value.lower() == 'quit':
            quit_program()

        print('\nThanks! You are now done with the application form and we will contact you as soon as possible!')

        # opening file with the customers name for section 1, that is going to be encoded.
        solecustomer_section1 = open(solecustomer_lastname + '_' + solecustomer_firstname + '_section1' + '.txt', 'w')


        # Writing all the information into the file.
        solecustomer_section1.write(
            'Customers name                  : ' + solecustomer_title + ' ' + solecustomer_lastname
            + ' ' + solecustomer_firstname + '\n')  # title + lastname + firstname for the customer.
        solecustomer_section1.write('Account usage                   : ' + solecustomer_account_usage + '\n')
        solecustomer_section1.write('Other names                     : ' + solecustomer_othername + '\n')
        solecustomer_section1.write('Date of birth                   : ' + solecustomer_dob + '\n')
        solecustomer_section1.write('Gender                          : ' + solecustomer_gender + '\n')
        solecustomer_section1.write('Employed                        : ' + solecustomer_occupation + '\n')
        solecustomer_section1.write('How long since last worked      : ' + solecustomer_unemployed + '\n')
        solecustomer_section1.write('Country of birth                : ' + solecustomer_cob + '\n')
        solecustomer_section1.write('Town/City of birth              : ' + solecustomer_tob + '\n')
        solecustomer_section1.write('Nationality                     : ' + solecustomer_nationality + '\n')
        solecustomer_section1.write('Addional nationalities          : ' + solecustomer_addionalnationality + '\n')
        solecustomer_section1.write('Country of residence            : ' + solecustomer_countryofresidence + '\n')
        solecustomer_section1.write('Countries as a tax resident     : ' + solecustomer_taxresident + '\n')

        # First page done.

        solecustomer_section1.write('Taxpayer ID Number (TIN)        : ' + solecustomer_tin + '\n')
        solecustomer_section1.write('Telephone Number (Home)         : ' + solecustomer_telephonenumber_home + '\n')
        solecustomer_section1.write('Telephone Number (Mobile)       : ' + solecustomer_telephonenumber_mobile + '\n')
        solecustomer_section1.write('Telephone Number (Work)         : ' + solecustomer_telephonenumber_work + '\n')
        solecustomer_section1.write('Residental home address         : ' + solecustomer_residentalhomeaddress + '\n')
        solecustomer_section1.write('Residental post code            : ' + solecustomer_residentalpostcode + '\n')
        solecustomer_section1.write('Residental Country              : ' + solecustomer_residentalcountry + '\n')
        solecustomer_section1.write('Date of residence               : ' + solecustomer_residentaldate + '\n')
        solecustomer_section1.write(
            'Moved last 3 years              : ' + solecustomer_previousresidental_question + '\n')
        solecustomer_section1.write(
            'Previous residence address      : ' + solecustomer_previousresidentalhomeadress + '\n')
        solecustomer_section1.write(
            'Previous residence postcode     : ' + solecustomer_previousresidentalpostcode + '\n')
        solecustomer_section1.write(
            'Previous residence country      : ' + solecustomer_previousresidentalcountry + '\n')
        solecustomer_section1.write('Correspondence at same address  : ' + solecustomer_correspondencresidental + '\n')
        solecustomer_section1.write(
            'Correspondence address          : ' + solecustomer_correspondencehomeaddress + '\n')
        solecustomer_section1.write('Correspondence postcode         : ' + solecustomer_correspondencepostcode + '\n')
        solecustomer_section1.write('Correspondence country          : ' + solecustomer_correspondencecountry + '\n')
        solecustomer_section1.close()

        # opening file with the customers name for rest of the sections.
        solecustomer_rest = open(solecustomer_lastname + '_' + solecustomer_firstname + '_rest' + '.txt', 'w')

        solecustomer_rest.write('Debitcard Yes/No                : ' + solecustomer_debitcard + '\n')
        solecustomer_rest.write('New Debit Card (NDC) name       : ' + solecustomer_newdebitcardname + '\n')
        solecustomer_rest.write('NDC Mothers previous name       : ' + solecustomer_newdebitcardmpn + '\n')
        solecustomer_rest.write('NDC date of birth               : ' + solecustomer_newdebitcarddob + '\n\n')

        # Second page is now done.

        solecustomer_rest.write('Marketing choices               \n')
        solecustomer_rest.write('Did the customer want any?      : ' + solecustomer_marketing_none + '\n\n')
        solecustomer_rest.write('Internet Banking                : ' + solecustomer_marketing_internetbanking + '\n')
        solecustomer_rest.write('Email                           : ' + solecustomer_marketing_email + '\n')
        solecustomer_rest.write('Post                            : ' + solecustomer_marketing_post + '\n')
        solecustomer_rest.write('Device messaging                : ' + solecustomer_marketing_devicemessaging + '\n')
        solecustomer_rest.write('Text messages                   : ' + solecustomer_marketing_textmessages + '\n')
        solecustomer_rest.write('Phone                           : ' + solecustomer_marketing_phone + '\n\n')

        solecustomer_rest.write('Additional personal and employment details               \n')
        solecustomer_rest.write('Is the customer working ?       : ' + solecustomer_working + '\n\n')
        solecustomer_rest.write('Working occupation              : ' + solecustomer_workingoccupation + '\n')
        solecustomer_rest.write('Working employers name          : ' + solecustomer_workingemployersname + '\n')
        solecustomer_rest.write('Working employers address       : ' + solecustomer_workingemployersaddress + '\n')
        solecustomer_rest.write('Working employers postcode      : ' + solecustomer_workingemployerspostcode + '\n')
        solecustomer_rest.write('How long worked for current     : ' + solecustomer_workingcurrentemployer + '\n')
        solecustomer_rest.write('How long worked for previous    : ' + solecustomer_workingpreviousemployer + '\n')
        solecustomer_rest.write(
            'Is the work pensionable ?       : ' + solecustomer_workingemploymentpensionable + '\n\n')

        solecustomer_rest.write('Income               \n')
        solecustomer_rest.write(
            'Salary/wages                    : ' + solecustomer_income_salaryfrequency + '_' + solecustomer_income_salary + '\n\n')
        solecustomer_rest.write(
            'Benefits                        : ' + solecustomer_income_benefitsfrequency + '_' + solecustomer_income_benefits + '\n')
        solecustomer_rest.write(
            'Pension                         : ' + solecustomer_income_pensionfrequency + '_' + solecustomer_income_pension + '\n')
        solecustomer_rest.write(
            'Investments                     : ' + solecustomer_income_investmentsfrequency + '_' + solecustomer_income_investments + '\n')
        solecustomer_rest.write(
            'Others                          : ' + solecustomer_income_othersfrequency + '_' + solecustomer_income_others + '\n')
        solecustomer_rest.write('Type of income the others are   : ' + solecustomer_income_othersspecify + '\n')
        solecustomer_rest.write('Monthly net income              : ' + solecustomer_income_monthly + '\n')
        solecustomer_rest.write('Monthly income on this account  : ' + solecustomer_income_monthlyaccount + '\n\n')

        solecustomer_rest.write('Commitments               \n')
        solecustomer_rest.write('Mortage                         : ' + solecustomer_commitments_mortgage + '\n')
        solecustomer_rest.write('HP/Loans                        : ' + solecustomer_commitments_loans + '\n')
        solecustomer_rest.write('Lloydsbankloans                 : ' + solecustomer_commitments_lloaydsbankloans + '\n')
        solecustomer_rest.write('Total monthly                   : ' + solecustomer_commitments_total + '\n\n')

        solecustomer_rest.write('Savings               \n')
        solecustomer_rest.write('No savings                                  : ' + solecustomer_nosavings + '\n')
        solecustomer_rest.write('Lloyds Bank savings only                    : ' + solecustomer_llbsavings + '\n')
        solecustomer_rest.write('LLoyds Bank and non-Lloyds Bank savings     : ' + solecustomer_llbnlbbsavings + '\n')
        solecustomer_rest.write('Non-Lloyds Bank savings only                : ' + solecustomer_nlbbsavings + '\n')
        solecustomer_rest.write('Total amount of savings                     : ' + solecustomer_totalsavings + '\n\n')

        solecustomer_rest.write('Banking details               \n')
        solecustomer_rest.write('Personal or business            : ' + solecustomer_bankingdetails + '\n')
        solecustomer_rest.write('What facility                   : ' + solecustomer_facilities + '\n')
        solecustomer_rest.write('How long have they banked there :  ' + solecustomer_facilitiestime + '\n')
        solecustomer_rest.write('Account to be closed            : ' + solecustomer_facilitiesclosed + '\n')
        solecustomer_rest.write('If no, why                      :  ' + solecustomer_facilitiesclosedwhy + '\n')
        solecustomer_rest.write('Like us to transfer them        : ' + solecustomer_facilitiestransfer + '\n\n')

        solecustomer_rest.write('Credit card details               \n')
        solecustomer_rest.write('Have credit card                : ' + solecustomer_creditcard + '\n')
        solecustomer_rest.write('Total of credit cards           : ' + solecustomer_creditcard_total + '\n')
        solecustomer_rest.write('Credit card limit               :  ' + solecustomer_creditcard_limit + '\n')
        solecustomer_rest.write('Lloyds Bank credit card         : ' + solecustomer_creditcard_lloyds + '\n')
        solecustomer_rest.write('Chargecard                      :  ' + solecustomer_creditcard_otherchargecard + '\n')
        solecustomer_rest.write('Storecard                       :  ' + solecustomer_creditcard_otherstorecard + '\n')
        solecustomer_rest.write('Other                           :  ' + solecustomer_creditcard_otherother + '\n')
        solecustomer_rest.write(
            'Specified if yes                : ' + solecustomer_creditcard_otherotherspecify + '\n\n')

        solecustomer_rest.write('Mortage details               \n')
        solecustomer_rest.write('Mortage                         : ' + solecustomer_mortgage + '\n')
        solecustomer_rest.write('With Lloyds                     : ' + solecustomer_mortgage_lloyds + '\n')
        solecustomer_rest.write('Outstanding balance on mortage  :  ' + solecustomer_mortgage_balance + '\n')
        solecustomer_rest.write('Value of house                  : ' + solecustomer_mortgage_value + '\n\n')
        solecustomer_rest.close()

        code = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'
            , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', '1', '2'
            , '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                '22', '23', '24', '25', '26'
            , '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                '44', '45', '46', '47', '48', '49'
            , '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66',
                '67', '68', '69', '70', '71', '72'
            , '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89',
                '90', '91', '92', '93', '94', '95'
            , '96', '97', '98', '99', '/', '102', '.', '101', '?', '(', ')']

        with open(solecustomer_lastname + '_' + solecustomer_firstname + '_section1' + '.txt', 'r') as file:
            data = file.read()

        rotN = 1
        encode = ''

        for a in range(len(data)):
            for b in range(len(code)):
                if data[a] == code[b]:
                    if b + rotN > 75:
                        diff = (b + rotN) - 75
                        encode = encode + (code[diff - 1])
                    else:
                        encode = encode + (code[b + rotN])

        encode1 = open(solecustomer_lastname + '_' + solecustomer_firstname + '_section_encoded' + '.txt', 'w')
        encode1.write(encode)

        import os
        os.remove(solecustomer_lastname + '_' + solecustomer_firstname + '_section1' + '.txt')

        quit_program()

    elif answer == '2':
        def quit_program():
            # Code to terminate the program.

            print('Thanks for visiting us today! Have a great day!')
            quit()


        def section3_info():  # prints ALL the info on section 3

            print('How we process your personal information\n\n'
                  'Who looks after your personal information:\nYour personal information will be held by Lloyds Bank Plc which is '
                  'part of the Lloyds Banking Group. More information on the Group can be found at www.lloydsbankinggroup.com\n\n'
                  'How we use your personal information\n\nWe will use your personal information:\n\n -To provide products and '
                  'services, manage your relationship with us and comply with any laws or regulations we are subject to (for '
                  'example the laws \nthat prevent financial crime or the regulatory requirements governing the products we '
                  'offer).\n -Other purposes including improving our services, exercising our rights in relation to agreements and '
                  'contracts and identifying products and services that may be of interest\n\nTo support us with the above we '
                  'analyse information we know about you and how you use our products and services, including some automated '
                  'decision making. \nYou can find out more about how we do this, and in what circumstances you can ask us to stop, '
                  'in our full privacy notice.\n\nWho we share your personal information with\n\nYour personal information will be '
                  'shared within Lloyds Banking Group and other companies that provide services to you or us, \nso that we and any '
                  'other companies in our Group can look after your relationship with us. \nBy sharing this information it enables '
                  'us to better understand our customers’ needs, run accounts and policies, and provide products and services '
                  'efficiently. \nThis processing may include activities which take place outside of the European Economic Area. '
                  '\nIf this is the case we will ensure appropriate safeguards are in place to protect your personal information. '
                  '\nYou can find out more about how we share your personal information with credit reference agencies below and '
                  'can access more information about how else we share your information in our full privacy notice.')

            print(
                'Where we collect your personal information from\n\nWe will collect personal information about you from a number '
                'of sources including:\n\n -Information given to us on application forms, when you talk to us in branch, over the '
                'phone or through the device you use and when new services are requested.\n -From analysis of how you operate our '
                'products and services, including the frequency, nature, location, origin and recipients of any payments\n -From '
                'or through other organisations (for example card associations, credit reference agencies, insurance companies, '
                'retailers, comparison websites, social media and fraud prevention agencies).\n -In certain circumstances '
                'we may also use information about health or criminal convictions but we will only do this where allowed by '
                'law or if you give us your consent.\n\nYou can find out more about where we collect personal information '
                'about you from in our full privacy notice.\n\nDo you have to give us your personal information\n\nWe may be '
                'required by law, or as a consequence of any contractual relationship we have, to collect certain personal '
                'information. \nFailure to provide this information may prevent or delay us fulfilling these obligations '
                'or performing services\n\nWhat rights you have over your personal information\n\nThe law gives you a number '
                'of rights in relation to your personal information including:\n\n -the right to access the personal information '
                'we have about you. This includes information from application forms, statements, correspondence '
                'and call recordings.\n -Thee right to get us to correct personal information that is wrong or incomplete.\n -In '
                'certain circumstances, the right to ask us to stop using or delete your personal information.\n -From 25 May '
                '2018 you will have the right to receive any personal information we have collected from you in an \n easily '
                're-usable format when it’s processed on certain grounds, such as consent or for contractual reasons. \n You '
                'can also ask us to pass this information on to another organisation.\n\nYou can find out more about these rights '
                'and how you can exercise them in our full privacy notice.\n\nOther Individuals you have financial links with\n\n'
                'We may also collect personal information about other individuals who you have a financial link with. \n'
                'This may include people who you have joint accounts or policies with such as your partner/spouse, dependents, '
                'beneficiaries or \npeople you have commercial links to, for example other directors or officers of your company.')

            print(
                '\nWe will collect this information to assess any applications, provide the services requested and to carry '
                'out credit reference and fraud prevention checks. \nYou can find out more about how we process personal '
                'information about individuals with whom you have a financial link in our full privacy notice\n\n'
                'How we use credit reference agencies\n\nIn order to process your application we may supply your personal '
                'information to credit reference agencies (CRAs) including how you use our \nproducts and '
                'services and they will give us information about you, such as about your financial history. '
                '\nWe do this to assess creditworthiness and product suitability, check your identity, '
                'manage your account, trace and recover debts and prevent criminal activity.\n\nWe may also continue to exchange '
                'information about you with CRAs on an ongoing basis, including about your settled accounts and '
                'any debts not fully repaid on time, \ninformation on funds going into the account, the balance on '
                'the account and, if you borrow, details of your repayments or whether you repay in full and on '
                'time. \nCRAs will share your information with other organisations, for example other organisations '
                'you ask to provide you with products and services. \nYour data will also be linked to the data of '
                'any joint applicants or other financial associates as explained above.\n\nYou can find out more about the '
                'identities of the CRAs, and the ways in which they use and share personal information, in our full '
                'privacy notice.\n\nHow we use fraud prevention agencies\n\nThe personal information we have collected from '
                'you and anyone you have a financial link with may be shared with fraud prevention agencies \nwho will use it '
                'to prevent fraud and money laundering and to verify your identity. If fraud is detected, you could be '
                'refused certain services, finance or employment. \nFurther details of how your information will be '
                'used by us and these fraud prevention agencies, and your data protection rights, can be found in '
                'our full privacy notice.')


        def section3_info2():

            print(
                'Our full privacy notice\n\nIt is important that you understand how the personal information you give us will '
                'be used. \nTherefore, we strongly advise that you read our full privacy notice, which you can find at '
                'http://www.lloydsbank.com/privacy.asp or you can ask us for a copy.\n\nHow you can contact us\n\nIf you have '
                'any questions or require more information about how we use your personal '
                'information please contact us using https://secure.lloydsbank.com/retail/contact_us/how-we-can-help.asp. '
                '\nYou can also call us on 0345 602 1997.\n\nIf you feel we have not answered your question Lloyds '
                'Banking Group has a Group Data Privacy Officer, who you can contact on 0345 602 1997 and tell us '
                'you want to speak to our Data Privacy Officer.\n\nVersion Control\n\nThis notice was last updated '
                'in February 2018')


        account_usage = input('\nYour information will now be store in a file.'
                              '\nYou can also type quit to end the application form at anytime.'
                              '\n\nWhat will you be using the Account for?')
        if account_usage.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            print(
                'Since you are doing an joint application, we will be alterlating between the two of you for each sections')
            solecustomer_random_question = input(
                '\n\n\nPlase read about how we process your personal information above.\nDo you agree? '
                '(Typing 2, no or quit will terminate your application)\n\n1. Yes\n2. No')

            if solecustomer_random_question == '1' or solecustomer_random_question.lower() == 'yes':
                break
            elif solecustomer_random_question == '2' or solecustomer_random_question.lower() == 'no':
                quit_program()
            elif solecustomer_random_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        while True:  # Loops the question
            solecustomer_existing_question = input(
                '\nPerfect! Let us start with the first customer. Are you an exisiting '
                'Lloids Bank customer?\n\n1. Yes \n2. No\n')

            if solecustomer_existing_question == '1' or solecustomer_existing_question == 'Yes':
                solecustomer_existing = 'Yes'
                break
            elif solecustomer_existing_question == '2' or solecustomer_existing_question == 'No':
                solecustomer_existing = 'No'
                break
            elif solecustomer_existing_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        while True:  # Loops the question
            solecustomer_title_question = input(
                '\nWhat is your title ?\n\n1. Mr.\n2. Mrs. \n3. Miss. \n4. Ms. \n\nIf other, please specify\n')

            if solecustomer_title_question == '1' or solecustomer_title_question == 'Mr.':
                solecustomer_title = 'Mr.'
                break
            elif solecustomer_title_question == '2' or solecustomer_title_question == 'Mrs.':
                solecustomer_title = 'Mrs.'
                break
            elif solecustomer_title_question == '3' or solecustomer_title_question == 'Miss.':
                solecustomer_title = 'Miss.'
                break
            elif solecustomer_title_question == '4' or solecustomer_title_question == 'Ms.':
                solecustomer_title = 'Ms.'
                break
            elif solecustomer_title_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer_title = solecustomer_title_question
                break

        solecustomer_lastname = input('\nWhat is your last name ?\n')
        if solecustomer_lastname.lower() == 'quit':
            quit_program()
        solecustomer_firstname = input('\nWhat is your first name ?\n')
        if solecustomer_firstname.lower() == 'quit':
            quit_program()

        print('\nPleasure to have you here today', solecustomer_title, solecustomer_lastname, solecustomer_firstname,
              '\nLet us continue with the application\n')  # printing title and name out to the applicant.

        while True:  # Loops the question
            solecustomer_othername_question = input(
                '\nAny other name you use/have used in the past?\n\n1. Yes \n2. No\n')

            if solecustomer_othername_question == '1' or solecustomer_othername_question == 'Yes':
                solecustomer_othername = input('Please specify.')
                break
            elif solecustomer_othername_question == '2' or solecustomer_othername_question == 'No':
                solecustomer_othername = 'No'
                break
            elif solecustomer_othername_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_dob = input('\nWhat is your date of birth?\n\nPlease format it like DDMMYY'
                                 '\nFor example 01 01 90 for being born 1st of Jan in 1990\n')
        if solecustomer_dob.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            solecustomer_gender_question = input(
                '\nWhat is your gender ?\n\nMale \nFemale \n\nIf other, please specify\n')

            if solecustomer_gender_question == '1' or solecustomer_gender_question == 'Male':
                solecustomer_gender = 'Male'
                break
            elif solecustomer_gender_question == '2' or solecustomer_gender_question == 'Female':
                solecustomer_gender = 'Female'
                break
            elif solecustomer_gender_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer_gender = solecustomer_gender_question
                break

        student_question = input('\nIf you are a student, you will only need to complete this '
                                 'form if you do not meet the criteria for a Student account'
                                 '\nType quit to terminate the process now or anything else to continue')
        if student_question.lower() == 'quit':
            quit_program()
        else:
            print('Lets continue\n')

        solecustomer_occupation = 'No'
        solecustomer_unemployed = 'N/A'

        while True:  # Loops the question
            solecustomer_occupation_question = input(
                '\nWhat is your occupation right now?\n\n1. Employed \n2. Self employed \n3. Part time \n'
                '4. Unemployed \n5. Not working \n6. Seeking work \n7. Retired \n8. Student'
                ' \n\nIf other, please specify\n')

            if solecustomer_occupation_question == '1' or solecustomer_occupation_question == 'Employed':
                solecustomer_occupation = 'Employed'
                break
            elif solecustomer_occupation_question == '2' or solecustomer_occupation_question == 'Self employed':
                solecustomer_occupation = 'Self employed'
                break
            elif solecustomer_occupation_question == '3' or solecustomer_occupation_question == 'Part time':
                solecustomer_occupation = 'Part time'
                break
            elif solecustomer_occupation_question == '4' or solecustomer_occupation_question == 'Unemployed':
                solecustomer_occupation = 'Unemployed'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '5' or solecustomer_occupation_question == 'Not working':
                solecustomer_occupation = 'Not working'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '6' or solecustomer_occupation_question == 'Seeking work':
                solecustomer_occupation = 'Seeking work'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '7' or solecustomer_occupation_question == 'Retired':
                solecustomer_occupation = 'Retired'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer_occupation_question == '8' or solecustomer_occupation_question == 'Student':
                solecustomer_occupation = 'Student'
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break

            elif solecustomer_occupation_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer_occupation_question = solecustomer_occupation_question
                solecustomer_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                '\nFor example 03 05 for being born three years and five months\n')
                break

        solecustomer_cob = input('\nYour country of birth ?\n')
        if solecustomer_cob.lower() == 'quit':
            quit_program()

        solecustomer_tob = input('\nYour Town/City of birth ?\n')
        if solecustomer_tob.lower() == 'quit':
            quit_program()

        solecustomer_nationality = input('\nWhat is your nationality ?\n')
        if solecustomer_nationality.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            solecustomer_addionalnationality_question = input(
                '\nDo you have any addional nationalities ?\n\n1. Yes\n2. No\n')

            if solecustomer_addionalnationality_question == '1' or solecustomer_addionalnationality_question == 'Yes':
                solecustomer_addionalnationality = input('Please specify.\n')
                break
            elif solecustomer_addionalnationality_question == '2' or solecustomer_addionalnationality_question == 'No':
                solecustomer_addionalnationality = 'No'
                break
            elif solecustomer_addionalnationality_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_countryofresidence = input('\nWhat is your country of residence ?\n')
        if solecustomer_nationality.lower() == 'quit':
            quit_program()

        solecustomer_taxresident = input(
            '\nWhich countries are you tax resident in ?\nPlease note: This is the country where '
            'an individual is resident under the tax laws of such jurisdiction\n')
        if solecustomer_taxresident.lower() == 'quit':
            quit_program()

        # First page done.

        solecustomer_tin = input('\nIf you have a Taxpayer Identification Number (TIN) for '
                                 'other countries, please provide details.\nGuidance: By TIN we mean, '
                                 'Taxpayer Identification number, or similar Tax payer reference number '
                                 'you hold for country(ies) you are tax resident in\n')
        if solecustomer_tin.lower() == 'quit':
            quit_program()

        # Defaulting the numbers to nothing until the user type something.
        solecustomer_telephonenumber_home = 'N/A'
        solecustomer_telephonenumber_mobile = 'N/A'
        solecustomer_telephonenumber_work = 'N/A'

        while True:  # Loops the question
            solecustomer_telephonenumber_question = input(
                '\nYour telephone numbers and area dialing codes ?\n\n1. Home\n2. Mobile\n3. Work')

            if solecustomer_telephonenumber_question == '1' or solecustomer_telephonenumber_question == 'Home':
                solecustomer_telephonenumber_home = input('Please specify.')
                solecustomer_telephonenumber_home_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer_telephonenumber_home_question.lower() == 'no' \
                        or solecustomer_telephonenumber_home_question == '2':
                    break

            elif solecustomer_telephonenumber_question == '2' or solecustomer_telephonenumber_question == 'Mobile':
                solecustomer_telephonenumber_mobile = input('Please specify.')
                solecustomer_telephonenumber_mobile_question = input('Would you like to fill in any other '
                                                                     'numbers?\n\n1. Yes\n2. No')
                if solecustomer_telephonenumber_mobile_question.lower() == 'no' \
                        or solecustomer_telephonenumber_mobile_question == '2':
                    break

            elif solecustomer_telephonenumber_question == '3' or solecustomer_telephonenumber_question == 'Work':
                solecustomer_telephonenumber_work = input('Please specify.')
                solecustomer_telephonenumber_work_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer_telephonenumber_work_question.lower() == 'no' \
                        or solecustomer_telephonenumber_work_question == '2':
                    break

            elif solecustomer_telephonenumber_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_residentalhomeaddress = input('\nYour home address (where you live)\n')
        if solecustomer_residentalhomeaddress.lower() == 'quit':
            quit_program()

        solecustomer_residentalpostcode = input('\nPostcode:\n')
        if solecustomer_residentalpostcode.lower() == 'quit':
            quit_program()

        solecustomer_residentalcountry = input('\nCountry:\n')
        if solecustomer_residentalcountry.lower() == 'quit':
            quit_program()

        solecustomer_residentaldate = input(
            '\When did you start living at this address ?\n\nPlease format it like MMYYYY'
            '\nFor example 011993 for starting living there January 1993\n')
        if solecustomer_residentaldate.lower() == 'quit':
            quit_program()

        # Setting to N/A in case user types No.
        solecustomer_previousresidentalhomeadress = 'N/A'
        solecustomer_previousresidentalpostcode = 'N/A'
        solecustomer_previousresidentalcountry = 'N/A'

        while True:  # Loops the question
            solecustomer_previousresidental_question = input(
                '\nHave you lived there less than three years ?\n\n1. Yes\n2. No\n')

            if solecustomer_previousresidental_question == '1' or solecustomer_previousresidental_question == 'Yes':
                solecustomer_previousresidentalhomeadress = input('\nYour previous address (where you lived)\n')
                if solecustomer_previousresidentalhomeadress.lower() == 'quit':
                    quit_program()
                solecustomer_previousresidentalpostcode = input('\nPostcode:\n')
                if solecustomer_previousresidentalpostcode.lower() == 'quit':
                    quit_program()
                solecustomer_previousresidentalcountry = input('\nCountry:\n')
                if solecustomer_previousresidentalcountry.lower() == 'quit':
                    quit_program()
                break
            elif solecustomer_previousresidental_question == '2' or solecustomer_previousresidental_question == 'No':
                solecustomer_previousresidental = 'No'
                break
            elif solecustomer_previousresidental_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again\n')

        # Sets them to N/A in case the user type No.
        solecustomer_correspondencehomeaddress = 'N/A'
        solecustomer_correspondencepostcode = 'N/A'
        solecustomer_correspondencecountry = 'N/A'
        solecustomer_correspondencresidental = 'N/A'

        while True:  # Loops the question
            solecustomer_correspondenceadress_question = input(
                '\nIs your correspondence address different from your current home address ?\n\n1. Yes\n2. No\n')

            if solecustomer_correspondenceadress_question == '1' or solecustomer_correspondenceadress_question == 'Yes':
                solecustomer_correspondencehomeaddress = input('\nYour correspondence address\n')
                if solecustomer_correspondencehomeaddress.lower() == 'quit':
                    quit_program()
                solecustomer_correspondencepostcode = input('\nPostcode:\n')
                if solecustomer_correspondencepostcode.lower() == 'quit':
                    quit_program()
                    solecustomer_correspondencecountry = input('\nCountry:\n')
                if solecustomer_correspondencecountry.lower() == 'quit':
                    quit_program()
                break
            elif solecustomer_correspondenceadress_question == '2' or solecustomer_correspondenceadress_question == 'No':
                solecustomer_correspondencresidental = 'No'
                break
            elif solecustomer_correspondenceadress_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again\n')

        while True:  # Loops the question
            solecustomer2_existing_question = input(
                '\nPerfect!, First customer have now finished section 1. Let us start wit'
                'h customer 2. Are you an exisiting Lloids Bank customer?\n\n1. Yes \n2. No\n')

            if solecustomer2_existing_question == '1' or solecustomer2_existing_question == 'Yes':
                solecustomer2_existing = 'Yes'
                break
            elif solecustomer2_existing_question == '2' or solecustomer2_existing_question == 'No':
                solecustomer2_existing = 'No'
                break
            elif solecustomer2_existing_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        while True:  # Loops the question
            solecustomer2_title_question = input(
                '\nWhat is your title ?\n\n1. Mr.\n2. Mrs. \n3. Miss. \n4. Ms. \n\nIf other, please specify\n')

            if solecustomer2_title_question == '1' or solecustomer2_title_question == 'Mr.':
                solecustomer2_title = 'Mr.'
                break
            elif solecustomer2_title_question == '2' or solecustomer2_title_question == 'Mrs.':
                solecustomer2_title = 'Mrs.'
                break
            elif solecustomer2_title_question == '3' or solecustomer2_title_question == 'Miss.':
                solecustomer2_title = 'Miss.'
                break
            elif solecustomer2_title_question == '4' or solecustomer2_title_question == 'Ms.':
                solecustomer2_title = 'Ms.'
                break
            elif solecustomer2_title_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer2_title = solecustomer2_title_question
                break

        solecustomer2_lastname = input('\nWhat is your last name ?\n')
        if solecustomer2_lastname.lower() == 'quit':
            quit_program()
        solecustomer2_firstname = input('\nWhat is your first name ?\n')
        if solecustomer2_firstname.lower() == 'quit':
            quit_program()

        print('\nPleasure to have you here today', solecustomer2_title, solecustomer2_lastname, solecustomer2_firstname,
              '\nLet us continue with the application\n')  # printing title and name out to the applicant.

        while True:  # Loops the question
            solecustomer2_othername_question = input(
                '\nAny other name you use/have used in the past?\n\n1. Yes \n2. No\n')

            if solecustomer2_othername_question == '1' or solecustomer2_othername_question == 'Yes':
                solecustomer2_othername = input('Please specify.')
                break
            elif solecustomer2_othername_question == '2' or solecustomer2_othername_question == 'No':
                solecustomer2_othername = 'No'
                break
            elif solecustomer2_othername_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer2_dob = input('\nWhat is your date of birth?\n\nPlease format it like DDMMYY'
                                  '\nFor example 01 01 90 for being born 1st of Jan in 1990\n')
        if solecustomer2_dob.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            solecustomer2_gender_question = input(
                '\nWhat is your gender ?\n\nMale \nFemale \n\nIf other, please specify\n')

            if solecustomer2_gender_question == '1' or solecustomer2_gender_question == 'Male':
                solecustomer2_gender = 'Male'
                break
            elif solecustomer2_gender_question == '2' or solecustomer2_gender_question == 'Female':
                solecustomer2_gender = 'Female'
                break
            elif solecustomer2_gender_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer2_gender = solecustomer2_gender_question
                break

        student_question = input('\nIf you are a student, you will only need to complete this '
                                 'form if you do not meet the criteria for a Student account'
                                 '\nType quit to terminate the process now or anything else to continue')
        if student_question.lower() == 'quit':
            quit_program()
        else:
            print('Lets continue\n')

        solecustomer2_occupation = 'No'
        solecustomer2_unemployed = 'N/A'

        while True:  # Loops the question
            solecustomer2_occupation_question = input(
                '\nWhat is your occupation right now?\n\n1. Employed \n2. Self employed \n3. Part time \n'
                '4. Unemployed \n5. Not working \n6. Seeking work \n7. Retired \n8. Student'
                ' \n\nIf other, please specify\n')

            if solecustomer2_occupation_question == '1' or solecustomer2_occupation_question == 'Employed':
                solecustomer2_occupation = 'Employed'
                break
            elif solecustomer2_occupation_question == '2' or solecustomer2_occupation_question == 'Self employed':
                solecustomer2_occupation = 'Self employed'
                break
            elif solecustomer2_occupation_question == '3' or solecustomer2_occupation_question == 'Part time':
                solecustomer2_occupation = 'Part time'
                break
            elif solecustomer2_occupation_question == '4' or solecustomer2_occupation_question == 'Unemployed':
                solecustomer2_occupation = 'Unemployed'
                solecustomer2_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                 '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer2_occupation_question == '5' or solecustomer2_occupation_question == 'Not working':
                solecustomer2_occupation = 'Not working'
                solecustomer2_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                 '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer2_occupation_question == '6' or solecustomer2_occupation_question == 'Seeking work':
                solecustomer2_occupation = 'Seeking work'
                solecustomer2_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                 '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer2_occupation_question == '7' or solecustomer2_occupation_question == 'Retired':
                solecustomer2_occupation = 'Retired'
                solecustomer2_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                 '\nFor example 03 05 for being born three years and five months\n')
                break
            elif solecustomer2_occupation_question == '8' or solecustomer2_occupation_question == 'Student':
                solecustomer2_occupation = 'Student'
                solecustomer2_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                 '\nFor example 03 05 for being born three years and five months\n')
                break

            elif solecustomer2_occupation_question.lower() == 'quit':
                quit_program()
            else:
                solecustomer2_occupation_question = solecustomer2_occupation_question
                solecustomer2_unemployed = input('\nHow long since you last worked ?\n\nPlease format it like YYMM'
                                                 '\nFor example 03 05 for being born three years and five months\n')
                break

        solecustomer2_cob = input('\nYour country of birth ?\n')
        if solecustomer2_cob.lower() == 'quit':
            quit_program()

        solecustomer2_tob = input('\nYour Town/City of birth ?\n')
        if solecustomer2_tob.lower() == 'quit':
            quit_program()

        solecustomer2_nationality = input('\nWhat is your nationality ?\n')
        if solecustomer2_nationality.lower() == 'quit':
            quit_program()

        while True:  # Loops the question
            solecustomer2_addionalnationality_question = input(
                '\nDo you have any addional nationalities ?\n\n1. Yes\n2. No\n')

            if solecustomer2_addionalnationality_question == '1' or solecustomer2_addionalnationality_question == 'Yes':
                solecustomer2_addionalnationality = input('Please specify.\n')
                break
            elif solecustomer2_addionalnationality_question == '2' or solecustomer2_addionalnationality_question == 'No':
                solecustomer2_addionalnationality = 'No'
                break
            elif solecustomer2_addionalnationality_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer2_countryofresidence = input('\nWhat is your country of residence ?\n')
        if solecustomer2_nationality.lower() == 'quit':
            quit_program()

        solecustomer2_taxresident = input(
            '\nWhich countries are you tax resident in ?\nPlease note: This is the country where '
            'an individual is resident under the tax laws of such jurisdiction\n')
        if solecustomer2_taxresident.lower() == 'quit':
            quit_program()

        # First page done.

        solecustomer2_tin = input('\nIf you have a Taxpayer Identification Number (TIN) for '
                                  'other countries, please provide details.\nGuidance: By TIN we mean, '
                                  'Taxpayer Identification number, or similar Tax payer reference number '
                                  'you hold for country(ies) you are tax resident in\n')
        if solecustomer2_tin.lower() == 'quit':
            quit_program()

        # Defaulting the numbers to nothing until the user type something.
        solecustomer2_telephonenumber_home = 'N/A'
        solecustomer2_telephonenumber_mobile = 'N/A'
        solecustomer2_telephonenumber_work = 'N/A'

        while True:  # Loops the question
            solecustomer2_telephonenumber_question = input(
                '\nYour telephone numbers and area dialing codes ?\n\n1. Home\n2. Mobile\n3. Work')

            if solecustomer2_telephonenumber_question == '1' or solecustomer2_telephonenumber_question == 'Home':
                solecustomer2_telephonenumber_home = input('Please specify.')
                solecustomer2_telephonenumber_home_question = input('Would you like to fill in any other '
                                                                    'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_telephonenumber_home_question.lower() == 'no' \
                        or solecustomer2_telephonenumber_home_question == '2':
                    break

            elif solecustomer2_telephonenumber_question == '2' or solecustomer2_telephonenumber_question == 'Mobile':
                solecustomer2_telephonenumber_mobile = input('Please specify.')
                solecustomer2_telephonenumber_mobile_question = input('Would you like to fill in any other '
                                                                      'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_telephonenumber_mobile_question.lower() == 'no' \
                        or solecustomer2_telephonenumber_mobile_question == '2':
                    break

            elif solecustomer2_telephonenumber_question == '3' or solecustomer2_telephonenumber_question == 'Work':
                solecustomer2_telephonenumber_work = input('Please specify.')
                solecustomer2_telephonenumber_work_question = input('Would you like to fill in any other '
                                                                    'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_telephonenumber_work_question.lower() == 'no' \
                        or solecustomer2_telephonenumber_work_question == '2':
                    break

            elif solecustomer2_telephonenumber_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer2_residentalhomeaddress = input('\nYour home address (where you live)\n')
        if solecustomer2_residentalhomeaddress.lower() == 'quit':
            quit_program()

        solecustomer2_residentalpostcode = input('\nPostcode:\n')
        if solecustomer2_residentalpostcode.lower() == 'quit':
            quit_program()

        solecustomer2_residentalcountry = input('\nCountry:\n')
        if solecustomer2_residentalcountry.lower() == 'quit':
            quit_program()

        solecustomer2_residentaldate = input(
            '\When did you start living at this address ?\n\nPlease format it like MMYYYY'
            '\nFor example 011993 for starting living there January 1993\n')
        if solecustomer2_residentaldate.lower() == 'quit':
            quit_program()

        # Setting to N/A in case user types No.
        solecustomer2_previousresidentalhomeadress = 'N/A'
        solecustomer2_previousresidentalpostcode = 'N/A'
        solecustomer2_previousresidentalcountry = 'N/A'

        while True:  # Loops the question
            solecustomer2_previousresidental_question = input(
                '\nHave you lived there less than three years ?\n\n1. Yes\n2. No\n')

            if solecustomer2_previousresidental_question == '1' or solecustomer2_previousresidental_question == 'Yes':
                solecustomer2_previousresidentalhomeadress = input('\nYour previous address (where you lived)\n')
                if solecustomer2_previousresidentalhomeadress.lower() == 'quit':
                    quit_program()
                solecustomer2_previousresidentalpostcode = input('\nPostcode:\n')
                if solecustomer2_previousresidentalpostcode.lower() == 'quit':
                    quit_program()
                solecustomer2_previousresidentalcountry = input('\nCountry:\n')
                if solecustomer2_previousresidentalcountry.lower() == 'quit':
                    quit_program()
                break
            elif solecustomer2_previousresidental_question == '2' or solecustomer2_previousresidental_question == 'No':
                solecustomer2_previousresidental = 'No'
                break
            elif solecustomer2_previousresidental_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again\n')

        # Sets them to N/A in case the user type No.
        solecustomer2_correspondencehomeaddress = 'N/A'
        solecustomer2_correspondencepostcode = 'N/A'
        solecustomer2_correspondencecountry = 'N/A'
        solecustomer2_correspondencresidental = 'N/A'

        while True:  # Loops the question
            solecustomer2_correspondenceadress_question = input(
                '\nIs your correspondence address different from your current home address ?\n\n1. Yes\n2. No\n')

            if solecustomer2_correspondenceadress_question == '1' or solecustomer2_correspondenceadress_question == 'Yes':
                solecustomer2_correspondencehomeaddress = input('\nYour correspondence address\n')
                if solecustomer2_correspondencehomeaddress.lower() == 'quit':
                    quit_program()
                solecustomer2_correspondencepostcode = input('\nPostcode:\n')
                if solecustomer2_correspondencepostcode.lower() == 'quit':
                    quit_program()
                    solecustomer2_correspondencecountry = input('\nCountry:\n')
                if solecustomer2_correspondencecountry.lower() == 'quit':
                    quit_program()
                break
            elif solecustomer2_correspondenceadress_question == '2' or solecustomer2_correspondenceadress_question == 'No':
                solecustomer2_correspondencresidental = 'No'
                break
            elif solecustomer2_correspondenceadress_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again\n')

        print('Let us go back to the first customer for section 2')

        solecustomer_debitcard = 'Yes'  # Defaulting to Yes

        # Defaulting to N/A in case user says no.
        solecustomer_newdebitcardname = 'N/A'
        solecustomer_newdebitcardmpn = 'N/A'
        solecustomer_newdebitcarddob = 'N/A'

        while True:  # Loops the question
            solecustomer_debitcard_question = input(
                '\nWould you like to apply for a debit card ?\n\n1. Yes\n2. No\n')

            if solecustomer_debitcard_question == '1' or solecustomer_debitcard_question == 'Yes':
                solecustomer_newdebitcard_question = input('\nAre you a new debit card customer ?\n\n1. Yes\n2. No\n')
                if solecustomer_newdebitcard_question == '1' or solecustomer_newdebitcard_question == 'Yes':
                    solecustomer_newdebitcardname = input('\nCustomer name to appear on card: \n')
                    if solecustomer_newdebitcardname.lower() == 'quit':
                        quit_program()
                    solecustomer_newdebitcardmpn = input('\nMothers previous name ? \n')
                    if solecustomer_newdebitcardmpn.lower() == 'quit':
                        quit_program()
                    solecustomer_newdebitcarddob = input('\nYour date of birth ?\n\nPlease format it like DDMMYY'
                                                         '\nFor example 010193 means you were born 1st of January in 1993\n')
                    if solecustomer_newdebitcarddob.lower() == 'quit':
                        quit_program()
                    break
                if solecustomer_newdebitcard_question == '2' or solecustomer_newdebitcard_question == 'No':
                    solecustomer_newdebitcardname = input('\nCustomer name to appear on card: \n')
                    if solecustomer_newdebitcardname.lower() == 'quit':
                        quit_program()
                    solecustomer_newdebitcarddob = input('\nYour date of birth ?\n\nPlease format it like DDMMYY'
                                                         '\nFor example 010193 means you were born 1st of January in 1993\n')
                    if solecustomer_newdebitcarddob.lower() == 'quit':
                        quit_program()
                    break
            elif solecustomer_debitcard_question == '2' or solecustomer_debitcard_question == 'No':
                solecustomer_debitcard = 'No'
                break
            elif solecustomer_debitcard_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        print('That was a quick section, let us start on the second customer for section 2')

        solecustomer2_debitcard = 'Yes'  # Defaulting to Yes

        # Defaulting to N/A in case user says no.
        solecustomer2_newdebitcardname = 'N/A'
        solecustomer2_newdebitcardmpn = 'N/A'
        solecustomer2_newdebitcarddob = 'N/A'

        while True:  # Loops the question
            solecustomer2_debitcard_question = input(
                '\nWould you like to apply for a debit card ?\n\n1. Yes\n2. No\n')

            if solecustomer2_debitcard_question == '1' or solecustomer2_debitcard_question == 'Yes':
                solecustomer2_newdebitcard_question = input('\nAre you a new debit card customer ?\n\n1. Yes\n2. No\n')
                if solecustomer2_newdebitcard_question == '1' or solecustomer2_newdebitcard_question == 'Yes':
                    solecustomer2_newdebitcardname = input('\nCustomer name to appear on card: \n')
                    if solecustomer2_newdebitcardname.lower() == 'quit':
                        quit_program()
                    solecustomer2_newdebitcardmpn = input('\nMothers previous name ? \n')
                    if solecustomer2_newdebitcardmpn.lower() == 'quit':
                        quit_program()
                    solecustomer2_newdebitcarddob = input('\nYour date of birth ?\n\nPlease format it like DDMMYY'
                                                          '\nFor example 010193 means you were born 1st of January in 1993\n')
                    if solecustomer2_newdebitcarddob.lower() == 'quit':
                        quit_program()
                    break
                if solecustomer2_newdebitcard_question == '2' or solecustomer2_newdebitcard_question == 'No':
                    solecustomer2_newdebitcardname = input('\nCustomer name to appear on card: \n')
                    if solecustomer2_newdebitcardname.lower() == 'quit':
                        quit_program()
                    solecustomer2_newdebitcarddob = input('\nYour date of birth ?\n\nPlease format it like DDMMYY'
                                                          '\nFor example 010193 means you were born 1st of January in 1993\n')
                    if solecustomer2_newdebitcarddob.lower() == 'quit':
                        quit_program()
                    break
            elif solecustomer2_debitcard_question == '2' or solecustomer2_debitcard_question == 'No':
                solecustomer2_debitcard = 'No'
                break
            elif solecustomer2_debitcard_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        print('Back to first customer as we are heading into the third section')

        section3_info()

        while True:  # Loops the question
            solecustomer_section3_question = input(
                '\n\n\nPlase read about how we process your personal information above.\n Do you agree? '
                '(Typing 2, no or quit will terminate your application)\n\n1. Yes\n2. No')

            if solecustomer_section3_question == '1' or solecustomer_section3_question.lower() == 'yes':
                break
            elif solecustomer_section3_question == '2' or solecustomer_section3_question.lower() == 'no':
                quit_program()
            elif solecustomer_section3_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Defaults answers to no
        solecustomer_marketing_internetbanking = 'No'
        solecustomer_marketing_email = 'No'
        solecustomer_marketing_post = 'No'
        solecustomer_marketing_devicemessaging = 'No'
        solecustomer_marketing_textmessages = 'No'
        solecustomer_marketing_phone = 'No'
        solecustomer_marketing_none = 'Yes'

        print('\nYour marketing choices\n\nWe would like to keep you up to date on products and offers that may '
              'be of interest to you. Please select how you would like to hear from us below. \nThese choices won’t affect '
              'any necessary information we need to send you such as statements and, don’t worry, you can change your mind '
              'and update your preferences at any time.')

        while True:  # Loops the question
            solecustomer_marketing_question = input(
                '\nAre you interested in any of these options ?\nType "done" or 8 when you are done selecting the ones '
                'you want.\n\n1. Internet Banking \n-You’ll see relevant messages when you log on to Internet Banking and our '
                'apps. If you do not pick this, you may still see messages, but they won’t be tailored to you.\n2. Em'
                'ail\n3. Post\n4. Device Messaging\n-You’ll receive relevant notifications to your mobile device\n5. Text messages\n6. Phone\n7. None'
                '\n8. Done\n\nBy saying yes you are giving consent for Lloyds Bank to use your personal information to send '
                'you relevant offers and products. \nLloyds Bank includes the following legal entities: Lloyds Bank plc; Lloyds '
                'Bank Insurance Services Ltd; and Halifax Share Dealing Limited.\n\nOccasionally we will send you selected '
                'offers from other companies within Lloyds Banking Group that may be relevant to you.')

            if solecustomer_marketing_question == '1':
                solecustomer_marketing_internetbanking = 'Yes'
            elif solecustomer_marketing_question == '2':
                solecustomer_marketing_email = 'Yes'
            elif solecustomer_marketing_question == '3':
                solecustomer_marketing_post = 'Yes'
            elif solecustomer_marketing_question == '4':
                solecustomer_marketing_devicemessaging = 'Yes'
            elif solecustomer_marketing_question == '5':
                solecustomer_marketing_textmessages = 'Yes'
            elif solecustomer_marketing_question == '6':
                solecustomer_marketing_phone = 'Yes'
            elif solecustomer_marketing_question == '7':
                solecustomer_marketing_none = 'None wanted'
                break
            elif solecustomer_marketing_question == '8' or solecustomer_marketing_question.lower() == 'done':
                break
            elif solecustomer_marketing_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        section3_info2()

        while True:  # Loops the question
            solecustomer_section3_question = input(
                '\n\n\nPlase read about how we process your personal information above.\nDo you agree? '
                '(Typing 2, no or quit will terminate your application)\n\n1. Yes\n2. No')

            if solecustomer_section3_question == '1' or solecustomer_section3_question.lower() == 'yes':
                break
            elif solecustomer_section3_question == '2' or solecustomer_section3_question.lower() == 'no':
                quit_program()
            elif solecustomer_section3_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')


        def quit_program():
            # Code to terminate the program.

            print('Thanks for visiting us today! Have a great day!')
            quit()


        print('With section 3 done for the first customer, it is now second customers turn to have a go at it')

        section3_info()

        while True:  # Loops the question
            solecustomer2_section3_question = input(
                '\n\n\nPlase read about how we process your personal information above.\n Do you agree? '
                '(Typing 2, no or quit will terminate your application)\n\n1. Yes\n2. No')

            if solecustomer2_section3_question == '1' or solecustomer2_section3_question.lower() == 'yes':
                break
            elif solecustomer2_section3_question == '2' or solecustomer2_section3_question.lower() == 'no':
                quit_program()
            elif solecustomer2_section3_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Defaults answers to no
        solecustomer2_marketing_internetbanking = 'No'
        solecustomer2_marketing_email = 'No'
        solecustomer2_marketing_post = 'No'
        solecustomer2_marketing_devicemessaging = 'No'
        solecustomer2_marketing_textmessages = 'No'
        solecustomer2_marketing_phone = 'No'
        solecustomer2_marketing_none = 'Yes'

        print('\nYour marketing choices\n\nWe would like to keep you up to date on products and offers that may '
              'be of interest to you. Please select how you would like to hear from us below. \nThese choices won’t affect '
              'any necessary information we need to send you such as statements and, don’t worry, you can change your mind '
              'and update your preferences at any time.')

        while True:  # Loops the question
            solecustomer2_marketing_question = input(
                '\nAre you interested in any of these options ?\nType "done" or 8 when you are done selecting the ones '
                'you want.\n\n1. Internet Banking \n-You’ll see relevant messages when you log on to Internet Banking and our '
                'apps. If you do not pick this, you may still see messages, but they won’t be tailored to you.\n2. Em'
                'ail\n3. Post\n4. Device Messaging\n-You’ll receive relevant notifications to your mobile device\n5. Text messages\n6. Phone\n7. None'
                '\n8. Done\n\nBy saying yes you are giving consent for Lloyds Bank to use your personal information to send '
                'you relevant offers and products. \nLloyds Bank includes the following legal entities: Lloyds Bank plc; Lloyds '
                'Bank Insurance Services Ltd; and Halifax Share Dealing Limited.\n\nOccasionally we will send you selected '
                'offers from other companies within Lloyds Banking Group that may be relevant to you.')

            if solecustomer2_marketing_question == '1':
                solecustomer2_marketing_internetbanking = 'Yes'
            elif solecustomer2_marketing_question == '2':
                solecustomer2_marketing_email = 'Yes'
            elif solecustomer2_marketing_question == '3':
                solecustomer2_marketing_post = 'Yes'
            elif solecustomer2_marketing_question == '4':
                solecustomer2_marketing_devicemessaging = 'Yes'
            elif solecustomer2_marketing_question == '5':
                solecustomer2_marketing_textmessages = 'Yes'
            elif solecustomer2_marketing_question == '6':
                solecustomer2_marketing_phone = 'Yes'
            elif solecustomer2_marketing_question == '7':
                solecustomer2_marketing_none = 'None wanted'
                break
            elif solecustomer2_marketing_question == '8' or solecustomer2_marketing_question.lower() == 'done':
                break
            elif solecustomer2_marketing_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        section3_info2()

        while True:  # Loops the question
            solecustomer2_section3_question = input(
                '\n\n\nPlase read about how we process your personal information above.\n Do you agree? '
                '(Typing 2, no or quit will terminate your application)\n\n1. Yes\n2. No')

            if solecustomer2_section3_question == '1' or solecustomer2_section3_question.lower() == 'yes':
                break
            elif solecustomer2_section3_question == '2' or solecustomer2_section3_question.lower() == 'no':
                quit_program()
            elif solecustomer2_section3_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')


        def quit_program():
            # Code to terminate the program.

            print('Thanks for visiting us today! Have a great day!')
            quit()


        # Predeterming some answers.

        solecustomer_section4_consent_signature = 'N/A'
        solecustomer_section4_statements_signature = 'N/A'
        solecustomer_section4_documentation_banking = 'No'
        solecustomer_section4_documentation_interestrates = 'No'
        solecustomer_section4_documentation_financial = 'No'
        solecustomer_section4_documentation_welcomepack = 'No'
        solecustomer_section4_documentation_brochure = 'No'

        print('Let us start with first customer going into the fourth section')

        print(
            'Current Accounts and Other Services\n\nThank you for opening your account with us. Your agreement is with '
            'Lloyds Bank plc.\n\nOur agreement with you is made up of general conditions (contained in the Personal '
            'banking terms and conditions leaflet) and additional conditions. \nThese include the conditions '
            'below and the Banking Charges guide which contains our standard fees. \nIf there is any overlap '
            'or conflict between the additional conditions and the Personal Banking terms and conditions, '
            'the additional conditions apply.\n\nEligibility\n\nTo have the account you must be 18 or over\n\nJoint Acco'
            'unts\n\nAll account holders can operate their accounts individually and are individually and jointly'
            ' liable for all amounts owed to us on those accounts. \nIt is important that you read the'
            ' Personal Banking terms and conditions as these explain how we deal with joint accounts'
            ' and your responsibilities.\n\nJoint Accounts - Preferential Rates\n\n -On some of our Savings products we offer '
            'higher preferential rates to customers based on their relationship with us, if they meet '
            'the qualifying criteria.\n -To check for the best rate we can offer on your account '
            'we will look at the products you hold with us and how you use them.\n -We will look at the products you and '
            'any person being added to your account hold individually and with each other. \n We will also look at products '
            'that you may each hold with other parties.\n -The rate will be based on which one of you meets the most '
            'qualifying criteria rather than the combined products you both hold.\n -In order to proceed the existing '
            'parties to the account must consent to us looking at all of the products they hold with the Bank. \n The party '
            'being added does not need to consent. \n Should only the existing parties consent, we '
            'will only be able to take their holdings into consideration (in addition to any holdings '
            'held jointly with the party being added) \n when working out the best rate you are collectively entitled to.\n'
            'When we confirm the rate for your account we will also tell you the relevant qualifying criteria.\n')

        while True:  # Loops the question
            solecustomer_section4_consent_question = input(
                '\nDo you con'
                'sent to share, with any other party to the account, details of any sole party holdings and any holdings '
                '\nyou may have in joint name with any other party in order that we can '
                'determine the best rate you are eligible for:\n\n1. Yes\n2. No\n')

            if solecustomer_section4_consent_question == '1' or solecustomer_section4_consent_question.lower() == 'yes':
                solecustomer_section4_consent = 'Yes'
                solecustomer_section4_consent_signature = input(
                    'Please type your name so we can compare it to the name given at the start')
                break
            elif solecustomer_section4_consent_question == '2' or solecustomer_section4_consent_question.lower() == 'no':
                solecustomer_section4_consent = 'no'
            elif solecustomer_section4_consent_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        print(
            'Bank statements\n\nWe will send account statements to both of you unless one of you signs here to say that '
            'you do not want us to send statements to you. \nYou can cancel this arrangement at any time by writing to us '
            'and we will then send separate statements to both of you.')

        while True:
            solecustomer_section4_statements_question = input(
                'Do you wish to stop receiving statements ?\n\n1. Yes\n2. No\n')
            if solecustomer_section4_statements_question == '1' or solecustomer_section4_statements_question == 'Yes':
                solecustomer_section4_statements = 'Yes'
                solecustomer_section4_statements_signature = input(
                    'Please type your name so we can compare it to the name given at the start')
                break
            if solecustomer_section4_statements_question == '2' or solecustomer_section4_statements_question == 'No':
                solecustomer_section4_statements = 'No'
                break
            elif solecustomer_section4_statements_question.lower() == 'quit': \
                    quit_program()
            else:
                print('\nInvalid entry, try again')

        while True:  # Loops the question
            solecustomer_section4_documentation_question = input(
                '\nWhich of the following documentation have you recieved ?\n\n1. Your banking relationship with us (the Pe'
                'rsonal Banking terms and conditions\n2. Advised and provided with Interest Rates Applicable to this Account\n'
                '3. Financial Services Compensation Scheme Information Sheet\n4. Welcome Pack\n5. Banking Charges Brochure')

            if solecustomer_section4_documentation_question == '1':
                solecustomer_section4_documentation_banking = 'Yes'
                solecustomer_section4_documentation_banking2 = input('Would you like to fill in any other '
                                                                     'numbers?\n\n1. Yes\n2. No')
                if solecustomer_section4_documentation_banking2.lower() == 'no' \
                        or solecustomer_section4_documentation_banking2 == '2':
                    solecustomer_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer_section4_documentation_banking2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_section4_documentation_question == '2':
                solecustomer_section4_documentation_interestrates = 'Yes'
                solecustomer_section4_documentation_interestrates2 = input('Would you like to fill in any other '
                                                                           'numbers?\n\n1. Yes\n2. No')
                if solecustomer_section4_documentation_interestrates2.lower() == 'no' \
                        or solecustomer_section4_documentation_interestrates2 == '2':
                    solecustomer_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer_section4_documentation_interestrates2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_section4_documentation_question == '3':
                solecustomer_section4_documentation_financial = 'Yes'
                solecustomer_section4_documentation_financial2 = input('Would you like to fill in any other '
                                                                       'numbers?\n\n1. Yes\n2. No')
                if solecustomer_section4_documentation_financial2.lower() == 'no' \
                        or solecustomer_section4_documentation_financial2 == '2':
                    solecustomer_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer_section4_documentation_financial2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_section4_documentation_question == '4':
                solecustomer_section4_documentation_welcomepack = 'Yes'
                solecustomer_section4_documentation_welcomepack2 = input('Would you like to fill in any other '
                                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer_section4_documentation_welcomepack2.lower() == 'no' \
                        or solecustomer_section4_documentation_welcomepack2 == '2':
                    solecustomer_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer_section4_documentation_welcomepack2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_section4_documentation_question == '5':
                solecustomer_section4_documentation_brochure = 'Yes'
                solecustomer_section4_documentation_brochure2 = input('Would you like to fill in any other '
                                                                      'numbers?\n\n1. Yes\n2. No')
                if solecustomer_section4_documentation_brochure2.lower() == 'no' \
                        or solecustomer_section4_documentation_brochure2 == '2':
                    solecustomer_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer_section4_documentation_brochure2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')

        solecustomer2_section4_consent_signature = 'N/A'
        solecustomer2_section4_statements_signature = 'N/A'
        solecustomer2_section4_documentation_banking = 'No'
        solecustomer2_section4_documentation_interestrates = 'No'
        solecustomer2_section4_documentation_financial = 'No'
        solecustomer2_section4_documentation_welcomepack = 'No'
        solecustomer2_section4_documentation_brochure = 'No'

        print('First customer have now finished the fourth section, it is up to you now second customer')

        print(
            'Current Accounts and Other Services\n\nThank you for opening your account with us. Your agreement is with '
            'Lloyds Bank plc.\n\nOur agreement with you is made up of general conditions (contained in the Personal '
            'banking terms and conditions leaflet) and additional conditions. \nThese include the conditions '
            'below and the Banking Charges guide which contains our standard fees. \nIf there is any overlap '
            'or conflict between the additional conditions and the Personal Banking terms and conditions, '
            'the additional conditions apply.\n\nEligibility\n\nTo have the account you must be 18 or over\n\nJoint Acco'
            'unts\n\nAll account holders can operate their accounts individually and are individually and jointly'
            ' liable for all amounts owed to us on those accounts. \nIt is important that you read the'
            ' Personal Banking terms and conditions as these explain how we deal with joint accounts'
            ' and your responsibilities.\n\nJoint Accounts - Preferential Rates\n\n -On some of our Savings products we offer '
            'higher preferential rates to customers based on their relationship with us, if they meet '
            'the qualifying criteria.\n -To check for the best rate we can offer on your account '
            'we will look at the products you hold with us and how you use them.\n -We will look at the products you and '
            'any person being added to your account hold individually and with each other. \n We will also look at products '
            'that you may each hold with other parties.\n -The rate will be based on which one of you meets the most '
            'qualifying criteria rather than the combined products you both hold.\n -In order to proceed the existing '
            'parties to the account must consent to us looking at all of the products they hold with the Bank. \n The party '
            'being added does not need to consent. \n Should only the existing parties consent, we '
            'will only be able to take their holdings into consideration (in addition to any holdings '
            'held jointly with the party being added) \n when working out the best rate you are collectively entitled to.\n'
            'When we confirm the rate for your account we will also tell you the relevant qualifying criteria.\n')

        while True:  # Loops the question
            solecustomer2_section4_consent_question = input(
                '\nDo you con'
                'sent to share, with any other party to the account, details of any sole party holdings and any holdings '
                '\nyou may have in joint name with any other party in order that we can '
                'determine the best rate you are eligible for:\n\n1. Yes\n2. No\n')

            if solecustomer2_section4_consent_question == '1' or solecustomer2_section4_consent_question.lower() == 'yes':
                solecustomer2_section4_consent = 'Yes'
                solecustomer2_section4_consent_signature = input(
                    'Please type your name so we can compare it to the name given at the start')
                break
            elif solecustomer2_section4_consent_question == '2' or solecustomer2_section4_consent_question.lower() == 'no':
                solecustomer2_section4_consent = 'no'
            elif solecustomer2_section4_consent_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        print(
            'Bank statements\n\nWe will send account statements to both of you unless one of you signs here to say that '
            'you do not want us to send statements to you. \nYou can cancel this arrangement at any time by writing to us '
            'and we will then send separate statements to both of you.')

        while True:
            solecustomer2_section4_statements_question = input(
                'Do you wish to stop receiving statements ?\n\n1. Yes\n2. No\n')
            if solecustomer2_section4_statements_question == '1' or solecustomer2_section4_statements_question == 'Yes':
                solecustomer2_section4_statements = 'Yes'
                solecustomer2_section4_statements_signature = input(
                    'Please type your name so we can compare it to the name given at the start')
                break
            if solecustomer2_section4_statements_question == '2' or solecustomer2_section4_statements_question == 'No':
                solecustomer2_section4_statements = 'No'
                break
            elif solecustomer2_section4_statements_question.lower() == 'quit': \
                    quit_program()
            else:
                print('\nInvalid entry, try again')

        while True:  # Loops the question
            solecustomer2_section4_documentation_question = input(
                '\nWhich of the following documentation have you recieved ?\n\n1. Your banking relationship with us (the Pe'
                'rsonal Banking terms and conditions\n2. Advised and provided with Interest Rates Applicable to this Account\n'
                '3. Financial Services Compensation Scheme Information Sheet\n4. Welcome Pack\n5. Banking Charges Brochure')

            if solecustomer2_section4_documentation_question == '1':
                solecustomer2_section4_documentation_banking = 'Yes'
                solecustomer2_section4_documentation_banking2 = input('Would you like to fill in any other '
                                                                      'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_section4_documentation_banking2.lower() == 'no' \
                        or solecustomer2_section4_documentation_banking2 == '2':
                    solecustomer2_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer2_section4_documentation_banking2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer2_section4_documentation_question == '2':
                solecustomer2_section4_documentation_interestrates = 'Yes'
                solecustomer2_section4_documentation_interestrates2 = input('Would you like to fill in any other '
                                                                            'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_section4_documentation_interestrates2.lower() == 'no' \
                        or solecustomer2_section4_documentation_interestrates2 == '2':
                    solecustomer2_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer2_section4_documentation_interestrates2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer2_section4_documentation_question == '3':
                solecustomer2_section4_documentation_financial = 'Yes'
                solecustomer2_section4_documentation_financial2 = input('Would you like to fill in any other '
                                                                        'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_section4_documentation_financial2.lower() == 'no' \
                        or solecustomer2_section4_documentation_financial2 == '2':
                    solecustomer2_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer2_section4_documentation_financial2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer2_section4_documentation_question == '4':
                solecustomer2_section4_documentation_welcomepack = 'Yes'
                solecustomer2_section4_documentation_welcomepack2 = input('Would you like to fill in any other '
                                                                          'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_section4_documentation_welcomepack2.lower() == 'no' \
                        or solecustomer2_section4_documentation_welcomepack2 == '2':
                    solecustomer2_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer2_section4_documentation_welcomepack2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer2_section4_documentation_question == '5':
                solecustomer2_section4_documentation_brochure = 'Yes'
                solecustomer2_section4_documentation_brochure2 = input('Would you like to fill in any other '
                                                                       'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_section4_documentation_brochure2.lower() == 'no' \
                        or solecustomer2_section4_documentation_brochure2 == '2':
                    solecustomer2_section4_documentation_signature = input(
                        'Please type your name so we can compare it to the name given at the start')
                    break
                elif solecustomer2_section4_documentation_brochure2.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')

        print('Let us head into the fifth section now customer one')

        solecustomer_workingoccupation = 'N/A'
        solecustomer_workingemployersname = 'N/A'
        solecustomer_workingemployersaddress = 'N/A'
        solecustomer_workingemployerspostcode = 'N/A'
        solecustomer_workingcurrentemployer = 'N/A'
        solecustomer_workingemploymentpensionable = 'N/A'

        while True:  # Loops the question
            solecustomer_working_question = input(
                '\nAre you currently working ?\n\n1. Yes \n2. No\n')

            if solecustomer_working_question == '1' or solecustomer_working_question == 'Yes':
                solecustomer_working = 'Yes'
                solecustomer_workingoccupation = input('What is your occupation ?')
                if solecustomer_workingoccupation.lower() == 'quit':
                    quit_program()
                solecustomer_workingemployersname = input('What is your employers name ?')
                if solecustomer_workingemployersname.lower() == 'quit':
                    quit_program()
                solecustomer_workingemployersaddress = input('What is your employers address ?')
                if solecustomer_workingemployersaddress.lower() == 'quit':
                    quit_program()
                solecustomer_workingemployerspostcode = input(
                    'What is the postcode (If known, type na if not available)')
                if solecustomer_workingemployerspostcode.lower() == 'quit':
                    quit_program()
                solecustomer_workingcurrentemployer = input('\nHow long have you worked for you curent empl'
                                                            'oyer ?\n\nPlease format it like YYMM'
                                                            '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer_workingcurrentemployer.lower() == 'quit':
                    quit_program()
                solecustomer_workingpreviousemployer = input('\nHow long did you work for your previous empl'
                                                             'oyer ?\n\nPlease format it like YYMM'
                                                             '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer_workingpreviousemployer.lower() == 'quit':
                    quit_program()
                solecustomer_workingemploymentpensionable_question = input(
                    'Is your employment pensionable ?\n\n1. Yes \n2. No\n')
                if solecustomer_workingemploymentpensionable_question == '1' or solecustomer_workingemploymentpensionable_question == 'Yes':
                    solecustomer_workingemploymentpensionable = 'Yes'
                    break
                elif solecustomer_workingemploymentpensionable_question == '2' or solecustomer_workingemploymentpensionable_question == 'No':
                    solecustomer_workingemploymentpensionable = 'No'
                    break
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_working_question == '2' or solecustomer_working_question == 'No':
                solecustomer_working = 'No'
                solecustomer_workingpreviousemployer = input('\nHow long did you work for your previous empl'
                                                             'oyer ?\n\nPlease format it like YYMM'
                                                             '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer_workingpreviousemployer.lower() == 'quit':
                    quit_program()
                    break
                break

        print('Customer one finishes up section 5 and it is now your turn customer two')

        solecustomer2_workingoccupation = 'N/A'
        solecustomer2_workingemployersname = 'N/A'
        solecustomer2_workingemployersaddress = 'N/A'
        solecustomer2_workingemployerspostcode = 'N/A'
        solecustomer2_workingcurrentemployer = 'N/A'
        solecustomer2_workingemploymentpensionable = 'N/A'

        while True:  # Loops the question
            solecustomer2_working_question = input(
                '\nAre you currently working ?\n\n1. Yes \n2. No\n')

            if solecustomer2_working_question == '1' or solecustomer2_working_question == 'Yes':
                solecustomer2_working = 'Yes'
                solecustomer2_workingoccupation = input('What is your occupation ?')
                if solecustomer2_workingoccupation.lower() == 'quit':
                    quit_program()
                solecustomer2_workingemployersname = input('What is your employers name ?')
                if solecustomer2_workingemployersname.lower() == 'quit':
                    quit_program()
                solecustomer2_workingemployersaddress = input('What is your employers address ?')
                if solecustomer2_workingemployersaddress.lower() == 'quit':
                    quit_program()
                solecustomer2_workingemployerspostcode = input(
                    'What is the postcode (If known, type na if not available)')
                if solecustomer2_workingemployerspostcode.lower() == 'quit':
                    quit_program()
                solecustomer2_workingcurrentemployer = input('\nHow long have you worked for you curent empl'
                                                             'oyer ?\n\nPlease format it like YYMM'
                                                             '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer2_workingcurrentemployer.lower() == 'quit':
                    quit_program()
                solecustomer2_workingpreviousemployer = input('\nHow long did you work for your previous empl'
                                                              'oyer ?\n\nPlease format it like YYMM'
                                                              '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer2_workingpreviousemployer.lower() == 'quit':
                    quit_program()
                solecustomer2_workingemploymentpensionable_question = input(
                    'Is your employment pensionable ?\n\n1. Yes \n2. No\n')
                if solecustomer2_workingemploymentpensionable_question == '1' or solecustomer2_workingemploymentpensionable_question == 'Yes':
                    solecustomer2_workingemploymentpensionable = 'Yes'
                    break
                elif solecustomer2_workingemploymentpensionable_question == '2' or solecustomer2_workingemploymentpensionable_question == 'No':
                    solecustomer2_workingemploymentpensionable = 'No'
                    break
                else:
                    print('\nInvalid entry, try again')
            if solecustomer2_working_question == '2' or solecustomer2_working_question == 'No':
                solecustomer2_working = 'No'
                solecustomer2_workingpreviousemployer = input('\nHow long did you work for your previous empl'
                                                              'oyer ?\n\nPlease format it like YYMM'
                                                              '\nFor example 03 05 for being born three years and five months\n')
                if solecustomer2_workingpreviousemployer.lower() == 'quit':
                    quit_program()
                    break
                break

        print('We are closing in on the end of the application, it is now first customer time to do the 6th section')

        # Predefine some answers unless changed.
        solecustomer_income_salaryfrequency = 'N/A'
        solecustomer_income_salary = 'N/A'
        solecustomer_income_benefitsfrequency = 'N/A'
        solecustomer_income_benefits = 'N/A'
        solecustomer_income_pensionfrequency = 'N/A'
        solecustomer_income_pension = 'N/A'
        solecustomer_income_investmentsfrequency = 'N/A'
        solecustomer_income_investments = 'N/A'
        solecustomer_income_othersfrequency = 'N/A'
        solecustomer_income_othersspecify = 'N/A'
        solecustomer_income_others = 'N/A'

        print('Income:')

        while True:  # Loops the question
            solecustomer_income_question = input(
                '\nIs any of the following source of your income ?\n\n1. Salary/wages\n2. Benefits\n3. Pension\n4. Inve'
                'stments\n5. Others')

            if solecustomer_income_question == '1' or solecustomer_income_question == 'Salary/wages':
                solecustomer_income_salaryfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_salarysource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_salarysource == '1':
                    solecustomer_income_salary = 'Direct to a bank'
                elif solecustomer_income_salarysource == '2':
                    solecustomer_income_salary = 'Cheque'
                elif solecustomer_income_salarysource == '3':
                    solecustomer_income_salary = 'Cash'
                elif solecustomer_income_salarysource == '4':
                    solecustomer_income_salary = 'Into this account'
                elif solecustomer_income_salarysource.lower() == 'quit':
                    quit_program()
                solecustomer_income_salarysource_question = input('Would you like to fill in any other '
                                                                  'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_salarysource_question.lower() == 'no' \
                        or solecustomer_income_salarysource_question == '2':
                    break
                elif solecustomer_income_salarysource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '2' or solecustomer_income_question == 'Benefits':
                solecustomer_income_benefitsfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_benefitssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_benefitssource == '1':
                    solecustomer_income_benefits = 'Direct to a bank'
                elif solecustomer_income_benefitssource == '2':
                    solecustomer_income_benefits = 'Cheque'
                elif solecustomer_income_benefitssource == '3':
                    solecustomer_income_benefits = 'Cash'
                elif solecustomer_income_benefitssource == '4':
                    solecustomer_income_benefits = 'Into this account'
                elif solecustomer_income_benefitssource.lower() == 'quit':
                    quit_program()
                solecustomer_income_benefitssource_question = input('Would you like to fill in any other '
                                                                    'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_benefitssource_question.lower() == 'no' \
                        or solecustomer_income_benefitssource_question == '2':
                    break
                elif solecustomer_income_benefitssource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '3' or solecustomer_income_question == 'Pension':
                solecustomer_income_pensionfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_pensionsource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_pensionsource == '1':
                    solecustomer_income_pension = 'Direct to a bank'
                elif solecustomer_income_pensionsource == '2':
                    solecustomer_income_pension = 'Cheque'
                elif solecustomer_income_pensionsource == '3':
                    solecustomer_income_pension = 'Cash'
                elif solecustomer_income_pensionsource == '4':
                    solecustomer_income_pension = 'Into this account'
                elif solecustomer_income_pensionsource.lower() == 'quit':
                    quit_program()
                solecustomer_income_pensionsource_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_pensionsource_question.lower() == 'no' \
                        or solecustomer_income_pensionsource_question == '2':
                    break
                elif solecustomer_income_pensionsource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '4' or solecustomer_income_question == 'Investments':
                solecustomer_income_investmentsfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_investmentssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_investmentssource == '1':
                    solecustomer_income_investments = 'Direct to a bank'
                elif solecustomer_income_investmentssource == '2':
                    solecustomer_income_investments = 'Cheque'
                elif solecustomer_income_investmentssource == '3':
                    solecustomer_income_investments = 'Cash'
                elif solecustomer_income_investmentssource == '4':
                    solecustomer_income_investments = 'Into this account'
                elif solecustomer_income_investmentssource.lower() == 'quit':
                    quit_program()
                solecustomer_income_investmentssource_question = input('Would you like to fill in any other '
                                                                       'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_investmentssource_question.lower() == 'no' \
                        or solecustomer_income_investmentssource_question == '2':
                    break
                elif solecustomer_income_investmentssource_question.lower() == 'quit':
                    quit_program()

            if solecustomer_income_question == '5' or solecustomer_income_question == 'Others':
                solecustomer_income_othersspecify = input('Please state type of income.')
                solecustomer_income_othersfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer_income_otherssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer_income_otherssource == '1':
                    solecustomer_income_others = 'Direct to a bank'
                elif solecustomer_income_otherssource == '2':
                    solecustomer_income_others = 'Cheque'
                elif solecustomer_income_otherssource == '3':
                    solecustomer_income_others = 'Cash'
                elif solecustomer_income_otherssource == '4':
                    solecustomer_income_others = 'Into this account'
                elif solecustomer_income_otherssource.lower() == 'quit':
                    quit_program()
                solecustomer_income_otherssource_question = input('Would you like to fill in any other '
                                                                  'numbers?\n\n1. Yes\n2. No')
                if solecustomer_income_otherssource_question.lower() == 'no' \
                        or solecustomer_income_otherssource_question == '2':
                    break
                elif solecustomer_income_otherssource_question.lower() == 'quit':
                    quit_program()

        solecustomer_income_monthly = input('How much is your total net monthly income?')
        solecustomer_income_monthlyaccount = input('How much are expected through this account per month ?')

        solecustomer_commitments_mortgage = input('\nWhat is your monthly commitments to Mortgage/rent ?\n')
        if solecustomer_commitments_mortgage.lower() == 'quit':
            quit_program()

        solecustomer_commitments_loans = input('\nWhat is your monthly commitments to HP/other loans ?\n')
        if solecustomer_commitments_loans.lower() == 'quit':
            quit_program()

        solecustomer_commitments_lloaydsbankloans = input(
            '\nWhat is your monthly commitments to Lloads Bank loans ?:\n')
        if solecustomer_commitments_lloaydsbankloans.lower() == 'quit':
            quit_program()

        solecustomer_commitments_total = input('\nWhat is your monthly commitments overall ?:\n')
        if solecustomer_commitments_total.lower() == 'quit':
            quit_program()

        print('With the 6th section done for the first customer, it is now your turn customer two to finish the 6th')

        # Predefine some answers unless changed.
        solecustomer2_income_salaryfrequency = 'N/A'
        solecustomer2_income_salary = 'N/A'
        solecustomer2_income_benefitsfrequency = 'N/A'
        solecustomer2_income_benefits = 'N/A'
        solecustomer2_income_pensionfrequency = 'N/A'
        solecustomer2_income_pension = 'N/A'
        solecustomer2_income_investmentsfrequency = 'N/A'
        solecustomer2_income_investments = 'N/A'
        solecustomer2_income_othersfrequency = 'N/A'
        solecustomer2_income_othersspecify = 'N/A'
        solecustomer2_income_others = 'N/A'

        print('Income:')

        while True:  # Loops the question
            solecustomer2_income_question = input(
                '\nIs any of the following source of your income ?\n\n1. Salary/wages\n2. Benefits\n3. Pension\n4. Inve'
                'stments\n5. Others')

            if solecustomer2_income_question == '1' or solecustomer2_income_question == 'Salary/wages':
                solecustomer2_income_salaryfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer2_income_salarysource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer2_income_salarysource == '1':
                    solecustomer2_income_salary = 'Direct to a bank'
                elif solecustomer2_income_salarysource == '2':
                    solecustomer2_income_salary = 'Cheque'
                elif solecustomer2_income_salarysource == '3':
                    solecustomer2_income_salary = 'Cash'
                elif solecustomer2_income_salarysource == '4':
                    solecustomer2_income_salary = 'Into this account'
                elif solecustomer2_income_salarysource.lower() == 'quit':
                    quit_program()
                solecustomer2_income_salarysource_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_income_salarysource_question.lower() == 'no' \
                        or solecustomer2_income_salarysource_question == '2':
                    break
                elif solecustomer2_income_salarysource_question.lower() == 'quit':
                    quit_program()

            if solecustomer2_income_question == '2' or solecustomer2_income_question == 'Benefits':
                solecustomer2_income_benefitsfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer2_income_benefitssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer2_income_benefitssource == '1':
                    solecustomer2_income_benefits = 'Direct to a bank'
                elif solecustomer2_income_benefitssource == '2':
                    solecustomer2_income_benefits = 'Cheque'
                elif solecustomer2_income_benefitssource == '3':
                    solecustomer2_income_benefits = 'Cash'
                elif solecustomer2_income_benefitssource == '4':
                    solecustomer2_income_benefits = 'Into this account'
                elif solecustomer2_income_benefitssource.lower() == 'quit':
                    quit_program()
                solecustomer2_income_benefitssource_question = input('Would you like to fill in any other '
                                                                     'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_income_benefitssource_question.lower() == 'no' \
                        or solecustomer2_income_benefitssource_question == '2':
                    break
                elif solecustomer2_income_benefitssource_question.lower() == 'quit':
                    quit_program()

            if solecustomer2_income_question == '3' or solecustomer2_income_question == 'Pension':
                solecustomer2_income_pensionfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer2_income_pensionsource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer2_income_pensionsource == '1':
                    solecustomer2_income_pension = 'Direct to a bank'
                elif solecustomer2_income_pensionsource == '2':
                    solecustomer2_income_pension = 'Cheque'
                elif solecustomer2_income_pensionsource == '3':
                    solecustomer2_income_pension = 'Cash'
                elif solecustomer2_income_pensionsource == '4':
                    solecustomer2_income_pension = 'Into this account'
                elif solecustomer2_income_pensionsource.lower() == 'quit':
                    quit_program()
                solecustomer2_income_pensionsource_question = input('Would you like to fill in any other '
                                                                    'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_income_pensionsource_question.lower() == 'no' \
                        or solecustomer2_income_pensionsource_question == '2':
                    break
                elif solecustomer2_income_pensionsource_question.lower() == 'quit':
                    quit_program()

            if solecustomer2_income_question == '4' or solecustomer2_income_question == 'Investments':
                solecustomer2_income_investmentsfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer2_income_investmentssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer2_income_investmentssource == '1':
                    solecustomer2_income_investments = 'Direct to a bank'
                elif solecustomer2_income_investmentssource == '2':
                    solecustomer2_income_investments = 'Cheque'
                elif solecustomer2_income_investmentssource == '3':
                    solecustomer2_income_investments = 'Cash'
                elif solecustomer2_income_investmentssource == '4':
                    solecustomer2_income_investments = 'Into this account'
                elif solecustomer2_income_investmentssource.lower() == 'quit':
                    quit_program()
                solecustomer2_income_investmentssource_question = input('Would you like to fill in any other '
                                                                        'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_income_investmentssource_question.lower() == 'no' \
                        or solecustomer2_income_investmentssource_question == '2':
                    break
                elif solecustomer2_income_investmentssource_question.lower() == 'quit':
                    quit_program()

            if solecustomer2_income_question == '5' or solecustomer2_income_question == 'Others':
                solecustomer2_income_othersspecify = input('Please state type of income.')
                solecustomer2_income_othersfrequency = input('\nFrequency e.g. weekly\n')
                solecustomer2_income_otherssource = input(
                    '\nWhere do you receive this source ?\n\n1. Direct to a bank\n2. Cheque\n3. Cash\n4. Into this account')
                if solecustomer2_income_otherssource == '1':
                    solecustomer2_income_others = 'Direct to a bank'
                elif solecustomer2_income_otherssource == '2':
                    solecustomer2_income_others = 'Cheque'
                elif solecustomer2_income_otherssource == '3':
                    solecustomer2_income_others = 'Cash'
                elif solecustomer2_income_otherssource == '4':
                    solecustomer2_income_others = 'Into this account'
                elif solecustomer2_income_otherssource.lower() == 'quit':
                    quit_program()
                solecustomer2_income_otherssource_question = input('Would you like to fill in any other '
                                                                   'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_income_otherssource_question.lower() == 'no' \
                        or solecustomer2_income_otherssource_question == '2':
                    break
                elif solecustomer2_income_otherssource_question.lower() == 'quit':
                    quit_program()

        solecustomer2_income_monthly = input('How much is your total net monthly income?')
        solecustomer2_income_monthlyaccount = input('How much are expected through this account per month ?')

        solecustomer2_commitments_mortgage = input('\nWhat is your monthly commitments to Mortgage/rent ?\n')
        if solecustomer2_commitments_mortgage.lower() == 'quit':
            quit_program()

        solecustomer2_commitments_loans = input('\nWhat is your monthly commitments to HP/other loans ?\n')
        if solecustomer2_commitments_loans.lower() == 'quit':
            quit_program()

        solecustomer2_commitments_lloaydsbankloans = input(
            '\nWhat is your monthly commitments to Lloads Bank loans ?:\n')
        if solecustomer2_commitments_lloaydsbankloans.lower() == 'quit':
            quit_program()

        solecustomer2_commitments_total = input('\nWhat is your monthly commitments overall ?:\n')
        if solecustomer2_commitments_total.lower() == 'quit':
            quit_program()

        print('Just a few more steps to go, first customer, it is time to start section 7')

        # Predefining some answers.
        solecustomer_nosavings = 'No'
        solecustomer_llbsavings = 'No'
        solecustomer_llbnlbbsavings = 'No'
        solecustomer_nlbbsavings = 'No'

        print('Savings:')

        while True:  # Loops the question
            solecustomer_savings_question = input(
                '\nWhat type of savings do you have ?\n\n1. No savings\n2. Lloyds Bank savings only\n3. LLoyds Bank and '
                'non-Lloyds Bank savings\n4. Non-Lloyds Bank savings only')

            if solecustomer_savings_question == '1':
                solecustomer_nosavings = 'Yes'
                solecustomer_nosavings_question = input('\nWould you like to fill in any other '
                                                        'numbers?\n\n1. Yes\n2. No')
                if solecustomer_nosavings_question.lower() == 'no' \
                        or solecustomer_nosavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_nosavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer_savings_question == '2':
                solecustomer_llbsavings = 'Yes'
                solecustomer_llbsavings_question = input('\nWould you like to fill in any other '
                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer_llbsavings_question.lower() == 'no' \
                        or solecustomer_llbsavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_llbsavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer_savings_question == '3':
                solecustomer_llbnlbbsavings = 'Yes'
                solecustomer_llbnlbbsavings_question = input('\nWould you like to fill in any other '
                                                             'numbers?\n\n1. Yes\n2. No')
                if solecustomer_llbnlbbsavings_question.lower() == 'no' \
                        or solecustomer_llbnlbbsavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_llbnlbbsavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer_savings_question == '4':
                solecustomer_nlbbsavings = 'Yes'
                solecustomer_nlbbsavings_question = input('\nWould you like to fill in any other '
                                                          'numbers?\n\n1. Yes\n2. No')
                if solecustomer_nlbbsavings_question.lower() == 'no' \
                        or solecustomer_nlbbsavings_question == '2':
                    solecustomer_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer_nlbbsavings_question.lower() == 'quit':
                    quit_program()

        print('With that done, customer two have to finish it as well')

        # Predefining some answers.
        solecustomer2_nosavings = 'No'
        solecustomer2_llbsavings = 'No'
        solecustomer2_llbnlbbsavings = 'No'
        solecustomer2_nlbbsavings = 'No'

        print('Savings:')

        while True:  # Loops the question
            solecustomer2_savings_question = input(
                '\nWhat type of savings do you have ?\n\n1. No savings\n2. Lloyds Bank savings only\n3. LLoyds Bank and '
                'non-Lloyds Bank savings\n4. Non-Lloyds Bank savings only')

            if solecustomer2_savings_question == '1':
                solecustomer2_nosavings = 'Yes'
                solecustomer2_nosavings_question = input('\nWould you like to fill in any other '
                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_nosavings_question.lower() == 'no' \
                        or solecustomer2_nosavings_question == '2':
                    solecustomer2_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer2_nosavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer2_savings_question == '2':
                solecustomer2_llbsavings = 'Yes'
                solecustomer2_llbsavings_question = input('\nWould you like to fill in any other '
                                                          'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_llbsavings_question.lower() == 'no' \
                        or solecustomer2_llbsavings_question == '2':
                    solecustomer2_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer2_llbsavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer2_savings_question == '3':
                solecustomer2_llbnlbbsavings = 'Yes'
                solecustomer2_llbnlbbsavings_question = input('\nWould you like to fill in any other '
                                                              'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_llbnlbbsavings_question.lower() == 'no' \
                        or solecustomer2_llbnlbbsavings_question == '2':
                    solecustomer2_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer2_llbnlbbsavings_question.lower() == 'quit':
                    quit_program()

            if solecustomer2_savings_question == '4':
                solecustomer2_nlbbsavings = 'Yes'
                solecustomer2_nlbbsavings_question = input('\nWould you like to fill in any other '
                                                           'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_nlbbsavings_question.lower() == 'no' \
                        or solecustomer2_nlbbsavings_question == '2':
                    solecustomer2_totalsavings = input('\nWhat is the total amount of your savings ?')
                    break
                elif solecustomer2_nlbbsavings_question.lower() == 'quit':
                    quit_program()

        print('Unto section 8 the last section, as customer one goes first')

        while True:  # Loops the question
            solecustomer_bankingdetails_question = input(
                'Is this a personal or business account?\n\n1. Personal\n2. Business\n')
            if solecustomer_bankingdetails_question == '1' or solecustomer_bankingdetails_question == 'Personal':
                solecustomer_bankingdetails = 'Personal'
                break
            elif solecustomer_bankingdetails_question == '2' or solecustomer_bankingdetails_question == 'Business':
                solecustomer_bankingdetails = 'Business'
                break
            elif solecustomer_bankingdetails_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Fixing potention answers.
        solecustomer_facilitiesclosedwhy = 'N/A'

        print('Other banking details:')

        while True:  # Loops the question
            solecustomer_facilities_question = input('\nWhich of the following facilitie'
                                                     's do you use: \n\n1. Cheque card\n2. Debit card\n')

            if solecustomer_facilities_question == '1' or solecustomer_facilities_question == 'Cheque card':
                solecustomer_facilities = 'Cheque card'
                solecustomer_facilitiestime = input(
                    '\nHow long have you banked there ?\n\nPlease format it like YYMM\nFor example 03 05 for be'
                    'ing born three years and five months\n')
                if solecustomer_facilitiestime.lower() == 'quit':
                    quit_program()
                solecustomer_facilitiesclosed_question = input('Is the account to be closed ?\n\n1. Yes\n2. No')
                if solecustomer_facilitiesclosed_question == '1' or solecustomer_facilitiesclosed_question == 'Yes':
                    solecustomer_facilitiesclosed = 'Yes'
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                        break
                elif solecustomer_facilitiesclosed_question == '2' or solecustomer_facilitiesclosed_question == 'No':
                    solecustomer_facilitiesclosed = 'No'
                    solecustomer_facilitiesclosedwhy = input('Please explain why\n')
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                        break
                    if solecustomer_facilitiestransfer_question == '2' or solecustomer_facilitiestransfer_question == 'No':
                        solecustomer_facilitiestransfer = 'No'
                        break
                elif solecustomer_facilitiesclosed_question.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer_facilities_question == '2' or solecustomer_facilities_question == 'Debit card':
                solecustomer_facilities = 'Cheque card'
                solecustomer_facilitiestime = input(
                    '\nHow long have you banked there ?\n\nPlease format it like YYMM\nFor example 03 05 for be'
                    'ing born three years and five months\n')
                if solecustomer_facilitiestime.lower() == 'quit':
                    quit_program()
                solecustomer_facilitiesclosed_question = input('Is the account to be closed ?\n\n1. Yes\n2. No')
                if solecustomer_facilitiesclosed_question == '1' or solecustomer_facilitiesclosed_question == 'Yes':
                    solecustomer_facilitiesclosed = 'Yes'
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                elif solecustomer_facilitiesclosed_question == '2' or solecustomer_facilitiesclosed_question == 'No':
                    solecustomer_facilitiesclosed = 'No'
                    solecustomer_facilitiesclosedwhy = input('Please explain why\n')
                    solecustomer_facilitiestransfer_question = input('Would you like us to trans'
                                                                     'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer_facilitiestransfer_question == '1' or solecustomer_facilitiestransfer_question == 'Yes':
                        solecustomer_facilitiestransfer = 'Yes'
                        break
                    if solecustomer_facilitiestransfer_question == '2' or solecustomer_facilitiestransfer_question == 'No':
                        solecustomer_facilitiestransfer = 'No'
                        break
                elif solecustomer_facilitiesclosed_question.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            elif solecustomer_facilities_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Predetermining some answers.
        solecustomer_creditcard_total = 'N/A'
        solecustomer_creditcard_limit = 'N/A'
        solecustomer_creditcard_lloyds = 'No'
        solecustomer_creditcard_otherchargecard = 'No'
        solecustomer_creditcard_otherstorecard = 'No'
        solecustomer_creditcard_otherother = 'No'
        solecustomer_creditcard_otherotherspecify = 'N/A'

        print('Your credit card detail:')

        while True:  # Loops the question
            solecustomer_creditcard_question = input('\nDo you hold a credit card? \n\n1. Yes\n2. No\n')

            if solecustomer_creditcard_question == '1' or solecustomer_creditcard_question == 'Yes':
                solecustomer_creditcard = 'Yes'
                solecustomer_creditcard_total = input('\nHow many do you have ? ')
                if solecustomer_creditcard_total.lower() == 'quit':
                    quit_program()
                solecustomer_creditcard_lloyds_question = input('\nAre any lloyds Bank ? \n\n1. Yes\n2. No\n')
                if solecustomer_creditcard_lloyds_question.lower() == 'quit':
                    quit_program()
                if solecustomer_creditcard_lloyds_question == '1' or solecustomer_creditcard_lloyds_question == 'Yes':
                    solecustomer_creditcard_lloyds = 'Yes'
                    solecustomer_creditcard_limit = input('What is your credit limit ?')
                    if solecustomer_creditcard_limit.lower() == 'quit':
                        quit_program()
                    break
                else:
                    break
            if solecustomer_creditcard_question == '2' or solecustomer_creditcard_question == 'No':
                solecustomer_creditcard = 'No'
                solecustomer_creditcard_lloyds_question = input('\nAre any lloyds Bank ? \n\n1. Yes\n2. No\n')
                if solecustomer_creditcard_lloyds_question.lower() == 'quit':
                    quit_program()
                if solecustomer_creditcard_lloyds_question == '1' or solecustomer_creditcard_lloyds_question == 'Yes':
                    solecustomer_creditcard_lloyds = 'Yes'
                    solecustomer_creditcard_limit = input('What is your credit limit ?')
                    if solecustomer_creditcard_limit.lower() == 'quit':
                        quit_program()
                    break
                else:
                    break
            else:
                print('\nInvalid entry, try again')

        while True:
            solecustomer_creditcard_other = input(
                'What other card type(s) do you hold ? \n\n1. Chargecard\n2. Storecard\n3. Other\n4. None')
            if solecustomer_creditcard_other == '1' or solecustomer_creditcard_other == 'Chargecard':
                solecustomer_creditcard_otherchargecard = 'Yes'
                solecustomer_creditcard_otherchargecard_question = input('\nWould you like to fill in any other '
                                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer_creditcard_otherchargecard_question == '2' or solecustomer_creditcard_otherchargecard_question == 'No':
                    break
            if solecustomer_creditcard_other == '2' or solecustomer_creditcard_other == 'Storecard':
                solecustomer_creditcard_otherstorecard = 'Yes'
                solecustomer_creditcard_otherstorecard_question = input('\nWould you like to fill in any other '
                                                                        'numbers?\n\n1. Yes\n2. No')
                if solecustomer_creditcard_otherstorecard_question == '2' or solecustomer_creditcard_otherchargecard_question == 'No':
                    break
            if solecustomer_creditcard_other == '3' or solecustomer_creditcard_other == 'Other':
                solecustomer_creditcard_otherother = 'Yes'
                solecustomer_creditcard_otherotherspecify = input('Please specify')
                solecustomer_creditcard_otherchargecard_question = input('\nWould you like to fill in any other '
                                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer_creditcard_otherchargecard_question == '2' or solecustomer_creditcard_otherchargecard_question == 'No':
                    break
            if solecustomer_creditcard_other == '4' or solecustomer_creditcard_other == 'None':
                break
            else:
                print('\nInvalid entry, try again')

        # Predetermining in case of answer
        solecustomer_mortgage_lloyds = 'No'

        print('Mortage details:')

        while True:  # Loops the question
            solecustomer_mortgage_question = input('\nDo you have a mortgage ?\n\n1. Yes\n2. No\n')

            if solecustomer_mortgage_question == '1' or solecustomer_mortgage_question == 'Yes':
                solecustomer_mortgage = 'Yes'
                solecustomer_mortgage_lloyds_question = input('\nIs it with Lloyds Bank ?\n\n1. Yes\n2. No\n')
                if solecustomer_mortgage_lloyds_question == '1' or solecustomer_mortgage_lloyds_question == 'Yes':
                    solecustomer_mortgage_lloyds = 'Yes'
                    break
                elif solecustomer_mortgage_lloyds_question.lower() == 'quit':
                    quit_program()
                else:
                    break
            if solecustomer_mortgage_question == '2' or solecustomer_mortgage_question == 'No':
                solecustomer_mortgage = 'No'
                break
            elif solecustomer_mortgage_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer_mortgage_balance = input('\nWhat is the outstanding balance on your mortgage?:\n')
        if solecustomer_mortgage_balance.lower() == 'quit':
            quit_program()

        solecustomer_mortgage_value = input('\nWhat is the value of your house?:\n')
        if solecustomer_mortgage_value.lower() == 'quit':
            quit_program()

        print('Customer one is now done with the application, it is now all down to customer two to finish this')

        while True:  # Loops the question
            solecustomer2_bankingdetails_question = input(
                'Is this a personal or business account?\n\n1. Personal\n2. Business\n')
            if solecustomer2_bankingdetails_question == '1' or solecustomer2_bankingdetails_question == 'Personal':
                solecustomer2_bankingdetails = 'Personal'
                break
            elif solecustomer2_bankingdetails_question == '2' or solecustomer2_bankingdetails_question == 'Business':
                solecustomer2_bankingdetails = 'Business'
                break
            elif solecustomer2_bankingdetails_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Fixing potention answers.
        solecustomer2_facilitiesclosedwhy = 'N/A'

        print('Other banking details:')

        while True:  # Loops the question
            solecustomer2_facilities_question = input('\nWhich of the following facilitie'
                                                      's do you use: \n\n1. Cheque card\n2. Debit card\n')

            if solecustomer2_facilities_question == '1' or solecustomer2_facilities_question == 'Cheque card':
                solecustomer2_facilities = 'Cheque card'
                solecustomer2_facilitiestime = input(
                    '\nHow long have you banked there ?\n\nPlease format it like YYMM\nFor example 03 05 for be'
                    'ing born three years and five months\n')
                if solecustomer2_facilitiestime.lower() == 'quit':
                    quit_program()
                solecustomer2_facilitiesclosed_question = input('Is the account to be closed ?\n\n1. Yes\n2. No')
                if solecustomer2_facilitiesclosed_question == '1' or solecustomer2_facilitiesclosed_question == 'Yes':
                    solecustomer2_facilitiesclosed = 'Yes'
                    solecustomer2_facilitiestransfer_question = input('Would you like us to trans'
                                                                      'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer2_facilitiestransfer_question == '1' or solecustomer2_facilitiestransfer_question == 'Yes':
                        solecustomer2_facilitiestransfer = 'Yes'
                        break
                elif solecustomer2_facilitiesclosed_question == '2' or solecustomer2_facilitiesclosed_question == 'No':
                    solecustomer2_facilitiesclosed = 'No'
                    solecustomer2_facilitiesclosedwhy = input('Please explain why\n')
                    solecustomer2_facilitiestransfer_question = input('Would you like us to trans'
                                                                      'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer2_facilitiestransfer_question == '1' or solecustomer2_facilitiestransfer_question == 'Yes':
                        solecustomer2_facilitiestransfer = 'Yes'
                        break
                    if solecustomer2_facilitiestransfer_question == '2' or solecustomer2_facilitiestransfer_question == 'No':
                        solecustomer2_facilitiestransfer = 'No'
                        break
                elif solecustomer2_facilitiesclosed_question.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            if solecustomer2_facilities_question == '2' or solecustomer2_facilities_question == 'Debit card':
                solecustomer2_facilities = 'Cheque card'
                solecustomer2_facilitiestime = input(
                    '\nHow long have you banked there ?\n\nPlease format it like YYMM\nFor example 03 05 for be'
                    'ing born three years and five months\n')
                if solecustomer2_facilitiestime.lower() == 'quit':
                    quit_program()
                solecustomer2_facilitiesclosed_question = input('Is the account to be closed ?\n\n1. Yes\n2. No')
                if solecustomer2_facilitiesclosed_question == '1' or solecustomer2_facilitiesclosed_question == 'Yes':
                    solecustomer2_facilitiesclosed = 'Yes'
                    solecustomer2_facilitiestransfer_question = input('Would you like us to trans'
                                                                      'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer2_facilitiestransfer_question == '1' or solecustomer2_facilitiestransfer_question == 'Yes':
                        solecustomer2_facilitiestransfer = 'Yes'
                elif solecustomer2_facilitiesclosed_question == '2' or solecustomer2_facilitiesclosed_question == 'No':
                    solecustomer2_facilitiesclosed = 'No'
                    solecustomer2_facilitiesclosedwhy = input('Please explain why\n')
                    solecustomer2_facilitiestransfer_question = input('Would you like us to trans'
                                                                      'fer your account ? \n\n1. Yes\n2. No\n')
                    if solecustomer2_facilitiestransfer_question == '1' or solecustomer2_facilitiestransfer_question == 'Yes':
                        solecustomer2_facilitiestransfer = 'Yes'
                        break
                    if solecustomer2_facilitiestransfer_question == '2' or solecustomer2_facilitiestransfer_question == 'No':
                        solecustomer2_facilitiestransfer = 'No'
                        break
                elif solecustomer2_facilitiesclosed_question.lower() == 'quit':
                    quit_program()
                else:
                    print('\nInvalid entry, try again')
            elif solecustomer2_facilities_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        # Predetermining some answers.
        solecustomer2_creditcard_total = 'N/A'
        solecustomer2_creditcard_limit = 'N/A'
        solecustomer2_creditcard_lloyds = 'No'
        solecustomer2_creditcard_otherchargecard = 'No'
        solecustomer2_creditcard_otherstorecard = 'No'
        solecustomer2_creditcard_otherother = 'No'
        solecustomer2_creditcard_otherotherspecify = 'N/A'

        print('Your credit card detail:')

        while True:  # Loops the question
            solecustomer2_creditcard_question = input('\nDo you hold a credit card? \n\n1. Yes\n2. No\n')

            if solecustomer2_creditcard_question == '1' or solecustomer2_creditcard_question == 'Yes':
                solecustomer2_creditcard = 'Yes'
                solecustomer2_creditcard_total = input('\nHow many do you have ? ')
                if solecustomer2_creditcard_total.lower() == 'quit':
                    quit_program()
                solecustomer2_creditcard_lloyds_question = input('\nAre any lloyds Bank ? \n\n1. Yes\n2. No\n')
                if solecustomer2_creditcard_lloyds_question.lower() == 'quit':
                    quit_program()
                if solecustomer2_creditcard_lloyds_question == '1' or solecustomer2_creditcard_lloyds_question == 'Yes':
                    solecustomer2_creditcard_lloyds = 'Yes'
                    solecustomer2_creditcard_limit = input('What is your credit limit ?')
                    if solecustomer2_creditcard_limit.lower() == 'quit':
                        quit_program()
                    break
                else:
                    break
            if solecustomer2_creditcard_question == '2' or solecustomer2_creditcard_question == 'No':
                solecustomer2_creditcard = 'No'
                solecustomer2_creditcard_lloyds_question = input('\nAre any lloyds Bank ? \n\n1. Yes\n2. No\n')
                if solecustomer2_creditcard_lloyds_question.lower() == 'quit':
                    quit_program()
                if solecustomer2_creditcard_lloyds_question == '1' or solecustomer2_creditcard_lloyds_question == 'Yes':
                    solecustomer2_creditcard_lloyds = 'Yes'
                    solecustomer2_creditcard_limit = input('What is your credit limit ?')
                    if solecustomer2_creditcard_limit.lower() == 'quit':
                        quit_program()
                    break
                else:
                    break
            else:
                print('\nInvalid entry, try again')

        while True:
            solecustomer2_creditcard_other = input(
                'What other card type(s) do you hold ? \n\n1. Chargecard\n2. Storecard\n3. Other\n4. None')
            if solecustomer2_creditcard_other == '1' or solecustomer2_creditcard_other == 'Chargecard':
                solecustomer2_creditcard_otherchargecard = 'Yes'
                solecustomer2_creditcard_otherchargecard_question = input('\nWould you like to fill in any other '
                                                                          'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_creditcard_otherchargecard_question == '2' or solecustomer2_creditcard_otherchargecard_question == 'No':
                    break
            if solecustomer2_creditcard_other == '2' or solecustomer2_creditcard_other == 'Storecard':
                solecustomer2_creditcard_otherstorecard = 'Yes'
                solecustomer2_creditcard_otherstorecard_question = input('\nWould you like to fill in any other '
                                                                         'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_creditcard_otherstorecard_question == '2' or solecustomer2_creditcard_otherstorecard_question == 'No':
                    break
            if solecustomer2_creditcard_other == '3' or solecustomer2_creditcard_other == 'Other':
                solecustomer2_creditcard_otherother = 'Yes'
                solecustomer2_creditcard_otherotherspecify = input('Please specify')
                solecustomer2_creditcard_otherchargecard_question = input('\nWould you like to fill in any other '
                                                                          'numbers?\n\n1. Yes\n2. No')
                if solecustomer2_creditcard_otherchargecard_question == '2' or solecustomer2_creditcard_otherchargecard_question == 'No':
                    break
            if solecustomer2_creditcard_other == '4' or solecustomer2_creditcard_other == 'None':
                break
            else:
                print('\nInvalid entry, try again')

        # Predetermining answer.
        solecustomer2_mortgage_lloyds = 'No'

        print('Mortage details:')

        while True:  # Loops the question
            solecustomer2_mortgage_question = input('\nDo you have a mortgage ?\n\n1. Yes\n2. No\n')

            if solecustomer2_mortgage_question == '1' or solecustomer2_mortgage_question == 'Yes':
                solecustomer2_mortgage = 'Yes'
                solecustomer2_mortgage_lloyds_question = input('\nIs it with Lloyds Bank ?\n\n1. Yes\n2. No\n')
                if solecustomer2_mortgage_lloyds_question == '1' or solecustomer2_mortgage_lloyds_question == 'Yes':
                    solecustomer2_mortgage_lloyds = 'Yes'
                    break
                elif solecustomer2_mortgage_lloyds_question.lower() == 'quit':
                    quit_program()
                else:
                    break
            if solecustomer2_mortgage_question == '2' or solecustomer2_mortgage_question == 'No':
                solecustomer2_mortgage = 'No'
                break
            elif solecustomer2_mortgage_question.lower() == 'quit':
                quit_program()
            else:
                print('\nInvalid entry, try again')

        solecustomer2_mortgage_balance = input('\nWhat is the outstanding balance on your mortgage?:\n')
        if solecustomer2_mortgage_balance.lower() == 'quit':
            quit_program()

        solecustomer2_mortgage_value = input('\nWhat is the value of your house?:\n')
        if solecustomer2_mortgage_value.lower() == 'quit':
            quit_program()

        print('\nThanks! You are now done with the application form and we will contact you as soon as possible!')

        # opening file with the customers name for section 1, that is going to be encoded.
        solecustomer_section1 = open(solecustomer_lastname + '_' + solecustomer_firstname + '_section1' + '.txt', 'w')

        # Writing all the information into the file.
        solecustomer_section1.write(
            'Customers name                  : ' + solecustomer_title + ' ' + solecustomer_lastname
            + ' ' + solecustomer_firstname + '\n')  # title + lastname + firstname for the customer.
        solecustomer_section1.write('Account usage                   : ' + account_usage + '\n')
        solecustomer_section1.write('Other names ?                   : ' + solecustomer_othername + '\n')
        solecustomer_section1.write('Date of birth                   : ' + solecustomer_dob + '\n')
        solecustomer_section1.write('Gender                          : ' + solecustomer_gender + '\n')
        solecustomer_section1.write('Employed ?                      : ' + solecustomer_occupation + '\n')
        solecustomer_section1.write('How long since last worked      : ' + solecustomer_unemployed + '\n')
        solecustomer_section1.write('Country of birth                : ' + solecustomer_cob + '\n')
        solecustomer_section1.write('Town/City of birth              : ' + solecustomer_tob + '\n')
        solecustomer_section1.write('Nationality                     : ' + solecustomer_nationality + '\n')
        solecustomer_section1.write('Addional nationalities          : ' + solecustomer_addionalnationality + '\n')
        solecustomer_section1.write('Country of residence            : ' + solecustomer_countryofresidence + '\n')
        solecustomer_section1.write('Countries as a tax resident     : ' + solecustomer_taxresident + '\n')

        # First page done.

        solecustomer_section1.write('Taxpayer ID Number (TIN)        : ' + solecustomer_tin + '\n')
        solecustomer_section1.write('Telephone Number (Home)         : ' + solecustomer_telephonenumber_home + '\n')
        solecustomer_section1.write('Telephone Number (Mobile)       : ' + solecustomer_telephonenumber_mobile + '\n')
        solecustomer_section1.write('Telephone Number (Work)         : ' + solecustomer_telephonenumber_work + '\n')
        solecustomer_section1.write('Residental home address         : ' + solecustomer_residentalhomeaddress + '\n')
        solecustomer_section1.write('Residental post code            : ' + solecustomer_residentalpostcode + '\n')
        solecustomer_section1.write('Residental Country              : ' + solecustomer_residentalcountry + '\n')
        solecustomer_section1.write('Date of residence               : ' + solecustomer_residentaldate + '\n')
        solecustomer_section1.write(
            'Moved last 3 years              : ' + solecustomer_previousresidental_question + '\n')
        solecustomer_section1.write(
            'Previous residence address      : ' + solecustomer_previousresidentalhomeadress + '\n')
        solecustomer_section1.write(
            'Previous residence postcode     : ' + solecustomer_previousresidentalpostcode + '\n')
        solecustomer_section1.write(
            'Previous residence country      : ' + solecustomer_previousresidentalcountry + '\n')
        solecustomer_section1.write('Correspondence at same address  : ' + solecustomer_correspondencresidental + '\n')
        solecustomer_section1.write(
            'Correspondence address          : ' + solecustomer_correspondencehomeaddress + '\n')
        solecustomer_section1.write('Correspondence postcode         : ' + solecustomer_correspondencepostcode + '\n')
        solecustomer_section1.write('Correspondence country          : ' + solecustomer_correspondencecountry + '\n')
        solecustomer_section1.close()

        # opening file with the customers name for rest of the sections.
        solecustomer_rest = open(solecustomer_lastname + '_' + solecustomer_firstname + '_rest' + '.txt', 'w')

        solecustomer_rest.write('Debitcard Yes/No                : ' + solecustomer_debitcard + '\n')
        solecustomer_rest.write('New Debit Card (NDC) name       : ' + solecustomer_newdebitcardname + '\n')
        solecustomer_rest.write('NDC Mothers previous name       : ' + solecustomer_newdebitcardmpn + '\n')
        solecustomer_rest.write('NDC date of birth               : ' + solecustomer_newdebitcarddob + '\n\n')

        # Second page is now done.

        solecustomer_rest.write('Marketing choices               \n')
        solecustomer_rest.write('Did the customer want any?      : ' + solecustomer_marketing_none + '\n\n')
        solecustomer_rest.write('Internet Banking                : ' + solecustomer_marketing_internetbanking + '\n')
        solecustomer_rest.write('Email                           : ' + solecustomer_marketing_email + '\n')
        solecustomer_rest.write('Post                            : ' + solecustomer_marketing_post + '\n')
        solecustomer_rest.write('Device messaging                : ' + solecustomer_marketing_devicemessaging + '\n')
        solecustomer_rest.write('Text messages                   : ' + solecustomer_marketing_textmessages + '\n')
        solecustomer_rest.write('Phone                           : ' + solecustomer_marketing_phone + '\n\n')

        solecustomer_rest.write('Agreement with us              \n')
        solecustomer_rest.write('Consent about joint account     : ' + solecustomer_section4_consent + '\n\n')
        solecustomer_rest.write('Signature if given              : ' + solecustomer_section4_consent_signature + '\n')
        solecustomer_rest.write('Bank statements, stop receiving : ' + solecustomer_section4_statements + '\n')
        solecustomer_rest.write(
            'Signature if given              : ' + solecustomer_section4_statements_signature + '\n')
        solecustomer_rest.write(
            'Banking relationship            : ' + solecustomer_section4_documentation_banking + '\n')
        solecustomer_rest.write(
            'Advised about Interest Rates    : ' + solecustomer_section4_documentation_interestrates + '\n')
        solecustomer_rest.write(
            'Financial Information Sheet     : ' + solecustomer_section4_documentation_financial + '\n')
        solecustomer_rest.write(
            'Welcome pack                    : ' + solecustomer_section4_documentation_welcomepack + '\n')
        solecustomer_rest.write(
            'Banking Brochure                : ' + solecustomer_section4_documentation_brochure + '\n')
        solecustomer_rest.write(
            'Signature                       : ' + solecustomer_section4_documentation_signature + '\n\n')

        solecustomer_rest.write('Additional personal and employment details               \n')
        solecustomer_rest.write('Is the customer working ?       : ' + solecustomer_working + '\n\n')
        solecustomer_rest.write('Working occupation              : ' + solecustomer_workingoccupation + '\n')
        solecustomer_rest.write('Working employers name          : ' + solecustomer_workingemployersname + '\n')
        solecustomer_rest.write('Working employers address       : ' + solecustomer_workingemployersaddress + '\n')
        solecustomer_rest.write('Working employers postcode      : ' + solecustomer_workingemployerspostcode + '\n')
        solecustomer_rest.write('How long worked for current     : ' + solecustomer_workingcurrentemployer + '\n')
        solecustomer_rest.write('How long worked for previous    : ' + solecustomer_workingpreviousemployer + '\n')
        solecustomer_rest.write(
            'Is the work pensionable ?       : ' + solecustomer_workingemploymentpensionable + '\n\n')

        solecustomer_rest.write('Income               \n')
        solecustomer_rest.write(
            'Salary/wages                    : ' + solecustomer_income_salaryfrequency + '_' + solecustomer_income_salary + '\n\n')
        solecustomer_rest.write(
            'Benefits                        : ' + solecustomer_income_benefitsfrequency + '_' + solecustomer_income_benefits + '\n')
        solecustomer_rest.write(
            'Pension                         : ' + solecustomer_income_pensionfrequency + '_' + solecustomer_income_pension + '\n')
        solecustomer_rest.write(
            'Investments                     : ' + solecustomer_income_investmentsfrequency + '_' + solecustomer_income_investments + '\n')
        solecustomer_rest.write(
            'Others                          : ' + solecustomer_income_othersfrequency + '_' + solecustomer_income_others + '\n')
        solecustomer_rest.write('Type of income the others are   : ' + solecustomer_income_othersspecify + '\n')
        solecustomer_rest.write('Monthly net income              : ' + solecustomer_income_monthly + '\n')
        solecustomer_rest.write('Monthly income on this account  : ' + solecustomer_income_monthlyaccount + '\n\n')

        solecustomer_rest.write('Commitments               \n')
        solecustomer_rest.write('Mortage                         : ' + solecustomer_commitments_mortgage + '\n')
        solecustomer_rest.write('HP/Loans                        : ' + solecustomer_commitments_loans + '\n')
        solecustomer_rest.write('Lloydsbankloans                 : ' + solecustomer_commitments_lloaydsbankloans + '\n')
        solecustomer_rest.write('Total monthly                   : ' + solecustomer_commitments_total + '\n\n')

        solecustomer_rest.write('Savings               \n')
        solecustomer_rest.write('No savings                                  : ' + solecustomer_nosavings + '\n')
        solecustomer_rest.write('Lloyds Bank savings only                    : ' + solecustomer_llbsavings + '\n')
        solecustomer_rest.write('LLoyds Bank and non-Lloyds Bank savings     : ' + solecustomer_llbnlbbsavings + '\n')
        solecustomer_rest.write('Non-Lloyds Bank savings only                : ' + solecustomer_nlbbsavings + '\n')
        solecustomer_rest.write('Total amount of savings                     : ' + solecustomer_totalsavings + '\n\n')

        solecustomer_rest.write('Banking details               \n')
        solecustomer_rest.write('Personal or business            : ' + solecustomer_bankingdetails + '\n')
        solecustomer_rest.write('What facility                   : ' + solecustomer_facilities + '\n')
        solecustomer_rest.write('How long have they banked there :  ' + solecustomer_facilitiestime + '\n')
        solecustomer_rest.write('Account to be closed            : ' + solecustomer_facilitiesclosed + '\n')
        solecustomer_rest.write('If no, why                      :  ' + solecustomer_facilitiesclosedwhy + '\n')
        solecustomer_rest.write('Like us to transfer them        : ' + solecustomer_facilitiestransfer + '\n\n')

        solecustomer_rest.write('Credit card details               \n')
        solecustomer_rest.write('Have credit card                : ' + solecustomer_creditcard + '\n')
        solecustomer_rest.write('Total of credit cards           : ' + solecustomer_creditcard_total + '\n')
        solecustomer_rest.write('Credit card limit               :  ' + solecustomer_creditcard_limit + '\n')
        solecustomer_rest.write('Lloyds Bank credit card         : ' + solecustomer_creditcard_lloyds + '\n')
        solecustomer_rest.write('Chargecard                      :  ' + solecustomer_creditcard_otherchargecard + '\n')
        solecustomer_rest.write('Storecard                       :  ' + solecustomer_creditcard_otherstorecard + '\n')
        solecustomer_rest.write('Other                           :  ' + solecustomer_creditcard_otherother + '\n')
        solecustomer_rest.write(
            'Specified if yes                : ' + solecustomer_creditcard_otherotherspecify + '\n\n')

        solecustomer_rest.write('Mortage details               \n')
        solecustomer_rest.write('Mortage                         : ' + solecustomer_mortgage + '\n')
        solecustomer_rest.write('With Lloyds                     : ' + solecustomer_mortgage_lloyds + '\n')
        solecustomer_rest.write('Outstanding balance on mortage  :  ' + solecustomer_mortgage_balance + '\n')
        solecustomer_rest.write('Value of house                  : ' + solecustomer_mortgage_value + '\n\n')
        solecustomer_rest.close()

        # opening file with the customers name for section 1, that is going to be encoded.
        solecustomer2_section1 = open(solecustomer2_lastname + '_' + solecustomer2_firstname + '_section1' + '.txt',
                                      'w')

        # Writing all the information into the file.
        solecustomer2_section1.write(
            'Customers name                  : ' + solecustomer2_title + ' ' + solecustomer2_lastname
            + ' ' + solecustomer2_firstname + '\n')  # title + lastname + firstname for the customer.
        solecustomer2_section1.write('Account usage                   : ' + account_usage + '\n')
        solecustomer2_section1.write('Other names ?                   : ' + solecustomer2_othername + '\n')
        solecustomer2_section1.write('Date of birth                   : ' + solecustomer2_dob + '\n')
        solecustomer2_section1.write('Gender                          : ' + solecustomer2_gender + '\n')
        solecustomer2_section1.write('Employed ?                      : ' + solecustomer2_occupation + '\n')
        solecustomer2_section1.write('How long since last worked      : ' + solecustomer2_unemployed + '\n')
        solecustomer2_section1.write('Country of birth                : ' + solecustomer2_cob + '\n')
        solecustomer2_section1.write('Town/City of birth              : ' + solecustomer2_tob + '\n')
        solecustomer2_section1.write('Nationality                     : ' + solecustomer2_nationality + '\n')
        solecustomer2_section1.write('Addional nationalities          : ' + solecustomer2_addionalnationality + '\n')
        solecustomer2_section1.write('Country of residence            : ' + solecustomer2_countryofresidence + '\n')
        solecustomer2_section1.write('Countries as a tax resident     : ' + solecustomer2_taxresident + '\n')

        # First page done.

        solecustomer2_section1.write('Taxpayer ID Number (TIN)        : ' + solecustomer2_tin + '\n')
        solecustomer2_section1.write('Telephone Number (Home)         : ' + solecustomer2_telephonenumber_home + '\n')
        solecustomer2_section1.write('Telephone Number (Mobile)       : ' + solecustomer2_telephonenumber_mobile + '\n')
        solecustomer2_section1.write('Telephone Number (Work)         : ' + solecustomer2_telephonenumber_work + '\n')
        solecustomer2_section1.write('Residental home address         : ' + solecustomer2_residentalhomeaddress + '\n')
        solecustomer2_section1.write('Residental post code            : ' + solecustomer2_residentalpostcode + '\n')
        solecustomer2_section1.write('Residental Country              : ' + solecustomer2_residentalcountry + '\n')
        solecustomer2_section1.write('Date of residence               : ' + solecustomer2_residentaldate + '\n')
        solecustomer2_section1.write(
            'Moved last 3 years              : ' + solecustomer2_previousresidental_question + '\n')
        solecustomer2_section1.write(
            'Previous residence address      : ' + solecustomer2_previousresidentalhomeadress + '\n')
        solecustomer2_section1.write(
            'Previous residence postcode     : ' + solecustomer2_previousresidentalpostcode + '\n')
        solecustomer2_section1.write(
            'Previous residence country      : ' + solecustomer2_previousresidentalcountry + '\n')
        solecustomer2_section1.write(
            'Correspondence at same address  : ' + solecustomer2_correspondencresidental + '\n')
        solecustomer2_section1.write(
            'Correspondence address          : ' + solecustomer2_correspondencehomeaddress + '\n')
        solecustomer2_section1.write('Correspondence postcode         : ' + solecustomer2_correspondencepostcode + '\n')
        solecustomer2_section1.write('Correspondence country          : ' + solecustomer2_correspondencecountry + '\n')
        solecustomer2_section1.close()

        # opening file with the customers name for rest of the sections.
        solecustomer2_rest = open(solecustomer2_lastname + '_' + solecustomer2_firstname + '_rest' + '.txt', 'w')

        solecustomer2_rest.write('Debitcard Yes/No                : ' + solecustomer2_debitcard + '\n')
        solecustomer2_rest.write('New Debit Card (NDC) name       : ' + solecustomer2_newdebitcardname + '\n')
        solecustomer2_rest.write('NDC Mothers previous name       : ' + solecustomer2_newdebitcardmpn + '\n')
        solecustomer2_rest.write('NDC date of birth               : ' + solecustomer2_newdebitcarddob + '\n\n')

        # Second page is now done.

        solecustomer2_rest.write('Marketing choices               \n')
        solecustomer2_rest.write('Did the customer want any?      : ' + solecustomer2_marketing_none + '\n\n')
        solecustomer2_rest.write('Internet Banking                : ' + solecustomer2_marketing_internetbanking + '\n')
        solecustomer2_rest.write('Email                           : ' + solecustomer2_marketing_email + '\n')
        solecustomer2_rest.write('Post                            : ' + solecustomer2_marketing_post + '\n')
        solecustomer2_rest.write('Device messaging                : ' + solecustomer2_marketing_devicemessaging + '\n')
        solecustomer2_rest.write('Text messages                   : ' + solecustomer2_marketing_textmessages + '\n')
        solecustomer2_rest.write('Phone                           : ' + solecustomer2_marketing_phone + '\n\n')

        solecustomer2_rest.write('Agreement with us              \n')
        solecustomer2_rest.write('Consent about joint account     : ' + solecustomer2_section4_consent + '\n\n')
        solecustomer2_rest.write('Signature if given              : ' + solecustomer2_section4_consent_signature + '\n')
        solecustomer2_rest.write('Bank statements, stop receiving : ' + solecustomer2_section4_statements + '\n')
        solecustomer2_rest.write(
            'Signature if given              : ' + solecustomer2_section4_statements_signature + '\n')
        solecustomer2_rest.write(
            'Banking relationship            : ' + solecustomer2_section4_documentation_banking + '\n')
        solecustomer2_rest.write(
            'Advised about Interest Rates    : ' + solecustomer2_section4_documentation_interestrates + '\n')
        solecustomer2_rest.write(
            'Financial Information Sheet     : ' + solecustomer2_section4_documentation_financial + '\n')
        solecustomer2_rest.write(
            'Welcome pack                    : ' + solecustomer2_section4_documentation_welcomepack + '\n')
        solecustomer2_rest.write(
            'Banking Brochure                : ' + solecustomer2_section4_documentation_brochure + '\n')
        solecustomer2_rest.write(
            'Signature                       : ' + solecustomer2_section4_documentation_signature + '\n\n')

        solecustomer2_rest.write('Additional personal and employment details               \n')
        solecustomer2_rest.write('Is the customer working ?       : ' + solecustomer2_working + '\n\n')
        solecustomer2_rest.write('Working occupation              : ' + solecustomer2_workingoccupation + '\n')
        solecustomer2_rest.write('Working employers name          : ' + solecustomer2_workingemployersname + '\n')
        solecustomer2_rest.write('Working employers address       : ' + solecustomer2_workingemployersaddress + '\n')
        solecustomer2_rest.write('Working employers postcode      : ' + solecustomer2_workingemployerspostcode + '\n')
        solecustomer2_rest.write('How long worked for current     : ' + solecustomer2_workingcurrentemployer + '\n')
        solecustomer2_rest.write('How long worked for previous    : ' + solecustomer2_workingpreviousemployer + '\n')
        solecustomer2_rest.write(
            'Is the work pensionable ?       : ' + solecustomer2_workingemploymentpensionable + '\n\n')

        solecustomer2_rest.write('Income               \n')
        solecustomer2_rest.write(
            'Salary/wages                    : ' + solecustomer2_income_salaryfrequency + '_' + solecustomer2_income_salary + '\n\n')
        solecustomer2_rest.write(
            'Benefits                        : ' + solecustomer2_income_benefitsfrequency + '_' + solecustomer2_income_benefits + '\n')
        solecustomer2_rest.write(
            'Pension                         : ' + solecustomer2_income_pensionfrequency + '_' + solecustomer2_income_pension + '\n')
        solecustomer2_rest.write(
            'Investments                     : ' + solecustomer2_income_investmentsfrequency + '_' + solecustomer2_income_investments + '\n')
        solecustomer2_rest.write(
            'Others                          : ' + solecustomer2_income_othersfrequency + '_' + solecustomer2_income_others + '\n')
        solecustomer2_rest.write('Type of income the others are   : ' + solecustomer2_income_othersspecify + '\n')
        solecustomer2_rest.write('Monthly net income              : ' + solecustomer2_income_monthly + '\n')
        solecustomer2_rest.write('Monthly income on this account  : ' + solecustomer2_income_monthlyaccount + '\n\n')

        solecustomer2_rest.write('Commitments               \n')
        solecustomer2_rest.write('Mortage                         : ' + solecustomer2_commitments_mortgage + '\n')
        solecustomer2_rest.write('HP/Loans                        : ' + solecustomer2_commitments_loans + '\n')
        solecustomer2_rest.write(
            'Lloydsbankloans                 : ' + solecustomer2_commitments_lloaydsbankloans + '\n')
        solecustomer2_rest.write('Total monthly                   : ' + solecustomer2_commitments_total + '\n\n')

        solecustomer2_rest.write('Savings               \n')
        solecustomer2_rest.write('No savings                                  : ' + solecustomer2_nosavings + '\n')
        solecustomer2_rest.write('Lloyds Bank savings only                    : ' + solecustomer2_llbsavings + '\n')
        solecustomer2_rest.write('LLoyds Bank and non-Lloyds Bank savings     : ' + solecustomer2_llbnlbbsavings + '\n')
        solecustomer2_rest.write('Non-Lloyds Bank savings only                : ' + solecustomer2_nlbbsavings + '\n')
        solecustomer2_rest.write('Total amount of savings                     : ' + solecustomer2_totalsavings + '\n\n')

        solecustomer2_rest.write('Banking details               \n')
        solecustomer2_rest.write('Personal or business            : ' + solecustomer2_bankingdetails + '\n')
        solecustomer2_rest.write('What facility                   : ' + solecustomer2_facilities + '\n')
        solecustomer2_rest.write('How long have they banked there :  ' + solecustomer2_facilitiestime + '\n')
        solecustomer2_rest.write('Account to be closed            : ' + solecustomer2_facilitiesclosed + '\n')
        solecustomer2_rest.write('If no, why                      :  ' + solecustomer2_facilitiesclosedwhy + '\n')
        solecustomer2_rest.write('Like us to transfer them        : ' + solecustomer2_facilitiestransfer + '\n\n')

        solecustomer2_rest.write('Credit card details               \n')
        solecustomer2_rest.write('Have credit card                : ' + solecustomer2_creditcard + '\n')
        solecustomer2_rest.write('Total of credit cards           : ' + solecustomer2_creditcard_total + '\n')
        solecustomer2_rest.write('Credit card limit               :  ' + solecustomer2_creditcard_limit + '\n')
        solecustomer2_rest.write('Lloyds Bank credit card         : ' + solecustomer2_creditcard_lloyds + '\n')
        solecustomer2_rest.write(
            'Chargecard                      :  ' + solecustomer2_creditcard_otherchargecard + '\n')
        solecustomer2_rest.write('Storecard                       :  ' + solecustomer2_creditcard_otherstorecard + '\n')
        solecustomer2_rest.write('Other                           :  ' + solecustomer2_creditcard_otherother + '\n')
        solecustomer2_rest.write(
            'Specified if yes                : ' + solecustomer2_creditcard_otherotherspecify + '\n\n')

        solecustomer2_rest.write('Mortage details               \n')
        solecustomer2_rest.write('Mortage                         : ' + solecustomer2_mortgage + '\n')
        solecustomer2_rest.write('With Lloyds                     : ' + solecustomer2_mortgage_lloyds + '\n')
        solecustomer2_rest.write('Outstanding balance on mortage  :  ' + solecustomer2_mortgage_balance + '\n')
        solecustomer2_rest.write('Value of house                  : ' + solecustomer2_mortgage_value + '\n\n')
        solecustomer2_rest.close()

        code = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'
            , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', '1', '2'
            , '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                '22', '23', '24', '25', '26'
            , '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                '44', '45', '46', '47', '48', '49'
            , '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66',
                '67', '68', '69', '70', '71', '72'
            , '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89',
                '90', '91', '92', '93', '94', '95'
            , '96', '97', '98', '99', '/', '102', '.', '101', '?', '(', ')']

        with open(solecustomer_lastname + '_' + solecustomer_firstname + '_section1' + '.txt', 'r') as file:
            data = file.read()

        rotN = 1
        encode = ''

        for a in range(len(data)):
            for b in range(len(code)):
                if data[a] == code[b]:
                    if b + rotN > 75:
                        diff = (b + rotN) - 75
                        encode = encode + (code[diff - 1])
                    else:
                        encode = encode + (code[b + rotN])

        encode1 = open(solecustomer_lastname + '_' + solecustomer_firstname + '_section1_encoded' + '.txt', 'w')
        encode1.write(encode)

        import os

        os.remove(solecustomer_lastname + '_' + solecustomer_firstname + '_section1' + '.txt')

        with open(solecustomer2_lastname + '_' + solecustomer2_firstname + '_section1' + '.txt', 'r') as file:
            data = file.read()

        rotN = 1
        encode = ''

        for a in range(len(data)):
            for b in range(len(code)):
                if data[a] == code[b]:
                    if b + rotN > 75:
                        diff = (b + rotN) - 75
                        encode = encode + (code[diff - 1])
                    else:
                        encode = encode + (code[b + rotN])

        encode1 = open(solecustomer2_lastname + '_' + solecustomer2_firstname + '_section1_encoded' + '.txt' + '.txt',
                       'w')
        encode1.write(encode)

        os.remove(solecustomer2_lastname + '_' + solecustomer2_firstname + '_section1' + '.txt')

        quit_program()

    elif answer == '3':
        quit_program()
    elif answer.lower() == 'quit':
        quit_program()
    else:
        print('\nInvalid input, please try again! ')