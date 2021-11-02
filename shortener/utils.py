import random

def shortened_url_generator(size=6, chars="1234567890qwertyuiopasdfghjklzxcvbnm"):
    return "".join(random.choice(chars) for _ in range(size))

def create_url(instance, size=6):
    URLShortener = instance
    url = shortened_url_generator(size=size)
    url_exists = URLShortener.objects.filter(shortened_url = url).exists()
    if url_exists:
        return create_url(size=6)
    return url
    