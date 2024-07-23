def check_link(link):
    if not link.startswith("http") and not link.startswith("https"):
        raise ValueError("'http' yoki 'https' bilan boshlanishi kerak!")
    print(f"{link}\n mavjud!")
check_link(link="https/instagram.com")