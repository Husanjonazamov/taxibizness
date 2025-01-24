def parse_text(lines):
        lines = [line.strip() for line in lines if line.strip()]  
        username = next((line.split(': ')[1] for line in lines if "Username" in line), None)
        count = next((line.split(': ')[1] for line in lines if "Yo'lovchi soni" in line), None)
        location = next((line.split(': ')[1] for line in lines if "Manzil" in line), None)
        phone_number = next((line.split(': ')[1] for line in lines if "Telefon" in line), None)
        
        return username, count, location, phone_number
    
    

def parse_mail_text(lines):
    lines = [line.strip() for line in lines if line.strip()]  # Bo'sh qatorlarni olib tashlaymiz
    username = next((line.split(': ')[1] for line in lines if "Username" in line), None)
    location = next((line.split(': ')[1] for line in lines if "Manzil" in line), None)
    phone_number = next((line.split(': ')[1] for line in lines if "Telefon" in line), None)
    return username, location, phone_number


def parse_mail_info(lines):
    lines = [line.strip() for line in lines if line.strip()]
    username = next((line.split(': ')[1] for line in lines if "Username" in line), None)
    application = next((line.split(': ')[1] for line in lines if "Ariza" in line), None)

    return username, application