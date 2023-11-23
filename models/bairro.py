from enum import Enum

class Bairro(Enum):
    POÇO = 'Poço'
    JARAGUÁ = 'Jaraguá'
    PONTA_DA_TERRA = 'Ponta da Terra'
    PAJUÇARA = 'Pajuçara'
    PONTA_VERDE = 'Ponta Verde'
    JATIÚCA = 'Jatiúca'
    MANGABEIRAS = 'Mangabeiras'

    CENTRO = 'Centro'
    PONTAL_DA_BARRA = 'Pontal da Barra'
    TRAPICHE = 'Trapiche'
    PRADO = 'Prado'
    PONTA_GROSSA = 'Ponta Grossa'
    LEVADA = 'Levada'
    VERGEL_DO_LAGO = 'Vergel do Lago'

    FAROL = 'Farol'
    PINTANGUINHA = 'Pintanguinha'
    PINHEIRO = 'Pinheiro'
    GRUTA_DE_LOURDES = 'Gruta de Lourdes'
    CANAÃ = 'Canaã'
    SANTO_AMARO = 'Santo Amaro'
    JARDIM_PETRÓPOLIS = 'Jardim Petrópolis'
    OURO_PRETO = 'Ouro Preto'

    BEBEDOURO = 'Bebedouro'
    C_DE_BEBEDOURO = 'C. de Bebedouro'
    C_DE_JAQUEIRA = 'C. de Jaqueira'
    BOM_PARTO = 'Bom Parto'
    PETRÓPOLIS = 'Petrópolis'
    STA_AMÉLIA = 'Sta. Amélia'
    FERNÃO_VELHO = 'Fernão Velho'
    RIO_NOVO = 'Rio Novo'
    MUTANGE = 'Mutange'

    JACINTINHO = 'Jacintinho'
    FEITOSA = 'Feitosa'
    BARRO_DURO = 'Barro Duro'
    SERRARIA = 'Serraria'
    SÃO_JORGE = 'São Jorge'

    BENEDITO_BENTES = 'Benedito Bentes'
    ANTARES = 'Antares'

    SANTOS_DUMONT = 'Santos Dumont'
    CLIMA_BOM = 'Clima Bom'
    CIDADE_UNIVERSITÁRIA = 'Cidade Universitária'
    SANTA_LÚCIA = 'Santa Lúcia'
    TABULEIRO_DOS_MARTINS = 'Tabuleiro dos Martins'
    
    JACARECICA = 'Jacarecica'
    GARÇA_TORTA = 'Garça Torta'
    CRUZ_DAS_ALMAS = 'Cruz das Almas'
    RIACHO_DOCE = 'Riacho Doce'
    PESCARIA = 'Pescaria'
    IPIOCA = 'Ipioca'

    @classmethod
    def pegar_bairro(cls, string):
        try:
            return cls(string)
        except:
            return None
    @classmethod
    def enumerar(cls):
        c = 0
        enumerado = {}
        for i in Bairro:
            enumerado[c] = i
            c+=1

        return enumerado

    @classmethod
    def encontrar_proximos(cls, bairro):
        bairros_enumerados = cls.enumerar()
        for bairro_ in bairros_enumerados.items():

            if bairro == bairro_[1]:
                bairro_pos = bairro_[0]
                bairro_instancia = bairro_[1]

           
                if bairro_pos >= 0 or bairro_pos <48:
                    bairro_pos_abaixo = bairro_pos + 1
                    bairro_instancia_abaixo = bairros_enumerados[bairro_pos_abaixo]
                if bairro_pos == 48:
                    bairro_pos_abaixo = bairro_pos
                    bairro_instancia_abaixo = bairros_enumerados[bairro_pos_abaixo]

                if bairro_pos >= 0 and bairro_pos < 48:
                    bairro_pos_acima = bairro_pos - 1
                    bairro_instancia_acima = bairros_enumerados[bairro_pos_acima]
                if bairro_pos == 48:
                    bairro_pos_acima = bairro_pos
                    bairro_instancia_acima = bairros_enumerados[bairro_pos_acima]
                
                return {
                    "acima": {"posicao": bairro_pos_acima, "instancia": bairro_instancia_acima},
                    "abaixo": {"posicao": bairro_pos_abaixo, "instancia": bairro_instancia_abaixo}
                }


