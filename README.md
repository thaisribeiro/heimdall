# 1. Heimdall

> Heimdall is the guardian of the rainbow bridge, which is the onlu way to Asgard (heaven) bouding with Midgard (earth) os nordic mithology, for this project Heimdall is responsible for not letting invalid bank data to be accepted.

![image](https://github.com/thaisribeiro/Heimdall/blob/feat%2Frefactoring/heimdall%2Fimage%2Fheimdall.png)

# 2. Validador de Contas Bancárias

Heimdall is a Python package which validates the main brazilian banks: Itaú, Bradesco, Caixa, Banco do Brasil, Citibank, Santander, Banrisul and Nubank.
For the remaining ones it is used a default validation:
* Agency is required to have 1 up to 5 digits
* Agency Branch is required to have 0 up to 2 characters
* Account is required to have 1 up to 12 digits
* Account Branch is required to have 0 up to 2 characters
# 3. Uso Básico

Instale com pip:
```
pip install heimdall
```


