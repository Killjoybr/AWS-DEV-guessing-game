import random

def lambda_handler(event, context):
    numero_secreto = random.randint(1, 10)
    palpite = int(event['queryStringParameters']['palpite'])

    if palpite < numero_secreto:
        resposta = "O numero eh maior. Tente novamente!"
    elif palpite > numero_secreto:
        resposta = "O numero eh menor. Tente novamente!"
    else:
        resposta = f"Parabens! Voce acertou o numero, o numero era {numero_secreto}!"

    return {
        'statusCode': 200,
        'body': f'{{"resultado": "{resposta}"}}'
    }
