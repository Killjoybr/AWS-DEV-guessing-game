# AWS-DEV-guessing-game

## Infraestrutura-AWS

### Lambda
Função serverless para lidar com a lógica do jogo.
<details>
    <summary>Função Lambda</summary>

![lambda com integração ao API Gateway](/assets/lambda.png)
</details><br>

```python
import random

def lambda_handler(event, context):
    numero_secreto = random.randint(1, 10)
    palpite = int(event['queryStringParameters']['palpite'])

    if palpite < numero_secreto:
        resposta = "O numero e maior. Tente novamente!"
    elif palpite > numero_secreto:
        resposta = "O numero e menor. Tente novamente!"
    else:
        resposta = f"Parabens! Voce acertou o numero {numero_secreto}!"

    return {
        'statusCode': 200,
        'body': f'{{"resultado": "{resposta}"}}'
    }
```

### API Gateway
API Gateway configurado com apenas uma rota para adivinhação e CORS com o princípio do menor privilégio, liberando acesso apenas para url do bucket com os protocolos http e https.
<details>
    <summary>API Gateway</summary>

![Rota API Gateway](/assets/gateway_route.png)

</details>

<details>
    <summary>Configuração do CORS</summary>

![CORS com princípio do menor privilégio](/assets/gateway_cors.png)
</details>

### S3
Bucket S3 configurado para hospedar o frontend estático.
<details>
    <summary>Bucket S3 do jogo</summary>

![Bucket S3 com o site estático](/assets/bucket.png)

</details>

<details>
    <summary>Opção de hospedagem estática do objeto</summary>

![Configuração S3 para hospedagem de site estático](/assets/s3static_host.png)

</details>

<details>
    <summary>Detalhamento da hospedagem estática</summary>

![Detalhamento da hospedagem S3 estática](/assets/s3_details.png)
</details>

## Agradecimentos

Agradeço ao professor Matheus Phillipo e toda equipe da [Escola da Nuvem](https://escoladanuvem.org/).
