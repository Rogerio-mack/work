# **Coeficientes no GLM (aplicados a experimentos de NIRS)**

Cada coeficiente estimado ($\beta$) corresponde ao quanto a variável explicativa (o preditor do seu design) está associada com a variação do sinal hemodinâmico (HbO ou HbR). Usando uma matriz de design baseada em regressão de eventos/blocos, cada $\beta$ reflete a magnitude da resposta hemodinâmica atribuída àquela condição:

> $\beta_{\text{condição A}}$ maior $\Rightarrow$ maior variação do sinal associada à condição A,

Os coeficientes são, portanto, uma forma de “força do efeito” ou “amplitude da resposta” do cérebro àquela condição experimental.

## **p-values**

O p-value associado a cada coeficiente testa a hipótese nula de que $\beta = 0$, ou seja, de que aquela condição não contribui significativamente para explicar a variação do sinal. Usualmente, consideramos significativo se  exige-se p-value $<
0.05$

<br>

</small>
Adicionalmente pode-se checar o `Pseudo R-square. (CS)`. Ideal, valores $> 0.9$, mostrando adequação da aplicação do modelo (cuidado para sobreajuste no caso de valores altos).

## **Análise nível Sujeito e Grupo**

As análises podem ser feitas em dois níveis. Nível Sujeito (1o Nível) e Nível de Grupo (2o Nível). Elas vão diferir um pouco na forma como empregamos e comparamos os $\beta$.

<br>
<br>

### **1. Análise de Ativação para uma Condição (Resposta $\times$ Baseline)**

### **1.1. Nível de Sujeito**

Se,

$$\beta_{\text{HBO, Condição A}} > 0  \space e \space \text{p-value} < 0.05 \space e $$

$$\beta_{\text{HBR, Condição A}} < 0 \space e \space \text{p-value}< 0.05 \Longrightarrow$$

<br>

Podemos concluir há evidências de que, **para aquele sujeito, a  condição A ativou o canal**.

<br>

---
<br>

> 🎯**Prático:**

> Essas condições já estão identificadas nas planilha `*_betas_GLM.xlsx` na sheet  `beta_<condição>`.

<br>

---

### **1.2. Nível de Grupo**

Pensando em nível de grupo, em um único canal de interesse e o seu beta para os vários sujeitos. Há ao menos duas abordagens para verificar se um canal é ativo para o grupo:

1. Testar $H_a:\hat\beta_{HBO} > 0$ ($H_0:\beta_{HBO} \le 0$)
com $\text{p-valor} < 0.05$;

>> e, mais rigorosa,

2. Testar
$H_a:\hat\beta_{HBO} > 0$ ($H_0:\beta_{HBO} \le 0$)
com $\text{p-valor} < 0.05$ e
$H_a:\hat\beta_{HBR} < 0$ ($H_0:\beta_{HBR} \ge 0$)
com $\text{p-valor} < 0.05$;

<br>


São **t-test unilaterais**.

Na segunda abordagem, como são testes conjuntos há ainda, para ser mais rigoroso, a necessidade de aplicarmos algum tipo de correção para redução de Falsos Positivos, como Bonferroni (muito conservador e não recomendado), FDR (false discovery rate), Hotelling's $T^2$ (o menos conservador).

<br>

---
<br>

> 🎯**Prático:**

> A sugestão é iniciarmos pelo mais fácil, **Abordagem 1 (somente HBO)**, o canal é ativo se o **`t-test unilateral`** (`ttest(betas, 0, 'Tail', 'right')`) é significativo. **Isso irá fornecer, inicialmente, mais canais ativos (Falsos Positivos)**. Os beta HBO já estão na planilha `*_betas_GLM.xlsx` na sheet  `beta_<condição>`.

> Depois, podemos refinar, empregando a **Abordagem 2 (HBO e HBR)**, com correção FDR (`mafdr(pvals, 'BHFDR', true)`) e/ou $T^2$:

>> a. para HBO/HBR.

>> b. para HBO/HBR + $m$ canais.

> sendo cada etapa mais conservadora e, potencialmente, apresentando menos canais ativos.

<br>

---

### **2. Análise de Ativação Maior entre duas Condições (Resposta A $\times$ Resposta B)**

Suponha agora duas condições A e B, e você deseja saber se amplitude de resposta atribuída à condição A é maior que à condição B. Para isso não é suficiente verificarmos $\beta_A > \beta_B$, mas é necessário fazer um teste estatístico de constraste.

### **Contraste**

1. Contraste $c = [1,-1]$
2. $H_0:\beta_A - \beta_B = 0$

Se $\text{p-value} < 0.05$, você rejeita $H_0$ e conclui que há evidências de diferença significativa entre os efeitos das tarefas A e B. O sinal do contraste (positivo/negativo) indicará qual tarefa teve maior resposta.

### **2.1. Nível de Sujeito**

No nível de sujeito, precisamos empregar os valores de covariância do GLM.


* Vetor de Contraste:

$$
c =
\begin{bmatrix}
1 \\ -1
\end{bmatrix},
\qquad
\hat{\delta} = c^\top \hat{\beta}.
$$

* Variância (do contraste):

$$
\mathrm{Var}(\hat{\delta})
= c^\top \Sigma_{\hat{\beta}}\, c
$$

* Erro padrão:

$$
\qquad
\mathrm{SE}(\hat{\delta})
= \sqrt{c^\top \Sigma_{\hat{\beta}}\, c}.
$$

* Estatística t:

$$
t = \frac{\hat{\delta}}{\mathrm{SE}(\hat{\delta})}.
$$

* p-valor (unilateral):

$$
p =\left(1 - F_{t,\nu}\left( |t| \right)\right),
$$

Ou se for um teste bicaudal, $p = 2\left(1 - F_{t,\nu}\left( |t| \right)\right)$.

<br>

onde $F_{t,\nu}$ é a função de distribuição acumulada (CDF) da distribuição t de Student com $\nu$ graus de liberdade.

<br>

---
<br>

> 🎯**Prático:**

> Este é caso mais difícil. Os beta contrast das duas condições, e as covariâncias e estatísticas t (uma para cada condição) também já estão na planilha `*_betas_GLM.xlsx` na sheet  `beta_contrast_ME`. Mas o cálculo ainda requer obter o grau de liberdade do GLM. Eu já vi como obter isso, mas isso ainda não está feito (não estava previsto). Depois, ainda tem que ser feito esses cálculos acima. Também eu poderia tentar empregar uma função do matlab `coefTest(mdl, C)` que já emprega o modelo GLM (`mdl`). Mas, de todos, é o mais complicado e vou precisar mais tempo para resolver...  

<br>

---

### **2.2. Nível de Grupo**

Pensando em nível de grupo e somente em termos de HBO, para cada sujeito $i$ calcularmos:

$$
d_i = \beta_{HBO, A, i} - \beta_{HBO, B, i}
$$

Fazemos então um t-test unilateral,

$$H_0:\mu_d \le 0$$
$$H_a:\mu_d > 0$$

Havendo vários canais, a rigor, também deveríamos aplicar uma correção (FDR, Bonferroni) dos valores do t-test como antes.

#### d-Cohen

Como um complemento, podemos depois calcular o tamanho do efeito com os betas:

$$
\text{d-Cohen} = \frac{\bar d}{s_d}
$$



<br>

---
<br>

> 🎯**Prático:**

> Os beta HBO A (Mãe) e betas HBO B (estranha) já estão na planilha `*_betas_GLM.xlsx` na sheet  `beta_contrast_ME`. Basta fazer as diferenças $d_i = \beta_{HBO, A, i} - \beta_{HBO, B, i}$ e aplicar o **`t-test unilateral`** (`ttest(d, 0, 'Tail', 'right')`). Os significativos serão o canais mais ativos para a condição A no nível de grupo.

> Deixar a correção FDR (ou outra) e análise d-Cohen para depois.

<br>

---



