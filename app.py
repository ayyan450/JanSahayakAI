while True:
    user = input("Aap: ").lower()

    if "passport" in user:
        print("AI: Passport se sambandhit madad ke liye Passport Seva Portal par apply karein.")

    elif "train" in user or "ticket" in user or "irctc" in user:
        print("AI: Train ticket IRCTC ke madhyam se book kiya jata hai.")

    elif "aadhar" in user or "aadhaar" in user:
        print("AI: Aadhaar ki sevaon ke liye UIDAI website ka upyog karein.")

    elif "pan" in user:
        print("AI: PAN card NSDL ya UTIITSL ke madhyam se ban sakta hai.")

    elif "hello" in user or "hi" in user or "namaste" in user:
        print("AI: Namaste! Main Jan Sahayak AI hoon.")

    elif "kaun ho" in user:
        print("AI: Main Jan Sahayak AI hoon, jo logon ki madad ke liye bana hai.")

    elif "exit" in user or "bye" in user:
        print("AI: Bye!")
        break

    else:
        print("AI: Kripya passport, train, aadhar ya PAN se sambandhit sawal puchhiye.")