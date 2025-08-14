#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Visual Proofs Generator
Gerador de Provas Visuais Instantâneas
"""

import time
import random
import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class VisualProofsGenerator:
    """Gerador de Provas Visuais Instantâneas"""

    def __init__(self):
        """Inicializa o gerador de provas visuais"""
        self.proof_types = self._load_proof_types()
        self.visual_elements = self._load_visual_elements()

        logger.info("Visual Proofs Generator inicializado")

    def _load_proof_types(self) -> Dict[str, Dict[str, Any]]:
        """Carrega tipos de provas visuais"""
        return {
            'antes_depois': {
                'nome': 'Transformação Antes/Depois',
                'objetivo': 'Mostrar transformação clara e mensurável',
                'impacto': 'Alto',
                'facilidade': 'Média'
            },
            'comparacao_competitiva': {
                'nome': 'Comparação vs Concorrência',
                'objetivo': 'Demonstrar superioridade clara',
                'impacto': 'Alto',
                'facilidade': 'Alta'
            },
            'timeline_resultados': {
                'nome': 'Timeline de Resultados',
                'objetivo': 'Mostrar progressão temporal',
                'impacto': 'Médio',
                'facilidade': 'Alta'
            },
            'social_proof_visual': {
                'nome': 'Prova Social Visual',
                'objetivo': 'Validação através de terceiros',
                'impacto': 'Alto',
                'facilidade': 'Média'
            },
            'demonstracao_processo': {
                'nome': 'Demonstração do Processo',
                'objetivo': 'Mostrar como funciona na prática',
                'impacto': 'Médio',
                'facilidade': 'Baixa'
            }
        }

    def _load_visual_elements(self) -> Dict[str, List[str]]:
        """Carrega elementos visuais disponíveis"""
        return {
            'graficos': ['Barras', 'Linhas', 'Pizza', 'Área', 'Dispersão'],
            'comparacoes': ['Lado a lado', 'Sobreposição', 'Timeline', 'Tabela'],
            'depoimentos': ['Vídeo', 'Texto', 'Áudio', 'Screenshot'],
            'demonstracoes': ['Screencast', 'Fotos', 'Infográfico', 'Animação'],
            'dados': ['Números', 'Percentuais', 'Valores', 'Métricas']
        }

    def generate_comprehensive_proofs(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any] = None, drivers: List[Dict] = None, session_id: str = None) -> Dict[str, Any]:
        """Gera provas visuais abrangentes e detalhadas"""
        try:
            logger.info("🎭 Gerando provas visuais abrangentes...")

            if not context_data:
                context_data = {}

            segmento = context_data.get('segmento', 'mercado')
            produto = context_data.get('produto', 'produto')

            # Conceitos para provas visuais
            conceitos_base = [
                f"Eficacia do {produto}",
                f"Transformacao no {segmento}",
                "Urgencia de acao",
                "Escassez temporal",
                "Prova social massiva",
                "Autoridade no mercado",
                "Simplicidade do metodo"
            ]

            provas_geradas = {}

            # Gera provas para cada conceito
            for i, conceito in enumerate(conceitos_base, 1):
                try:
                    prova = self._generate_single_prova_with_ai(conceito, avatar_data, context_data)
                    if prova:
                        prova_key = f"prova_{i}_{conceito.lower().replace(' ', '_')}"
                        provas_geradas[prova_key] = prova
                        logger.info(f"✅ Prova visual {i} gerada: {conceito}")
                    else:
                        # Fallback para prova basica
                        provas_geradas[f"prova_{i}_basica"] = self._create_basic_prova(conceito, segmento, produto)

                except Exception as e:
                    logger.error(f"❌ Erro ao gerar prova {i}: {e}")
                    # Fallback
                    provas_geradas[f"prova_{i}_fallback"] = self._create_basic_prova(conceito, segmento, produto)

            # Validacao e melhoria
            provas_validadas = {}
            for key, prova in provas_geradas.items():
                if self._validate_prova_quality(prova, context_data):
                    provas_validadas[key] = prova

            # Garantir minimo de 5 provas
            if len(provas_validadas) < 5:
                for i in range(len(provas_validadas), 5):
                    conceito_extra = f"Beneficio adicional {i+1}"
                    provas_validadas[f"prova_extra_{i+1}"] = self._create_basic_prova(conceito_extra, segmento, produto)

            return {
                'success': True,
                'total_provas': len(provas_validadas),
                'provas_visuais': provas_validadas,
                'segmento': segmento,
                'produto': produto,
                'metadata': {
                    'generated_at': datetime.now().isoformat(),
                    'ai_generated': len([p for p in provas_validadas.values() if p.get('ai_generated', False)]),
                    'fallback_generated': len([p for p in provas_validadas.values() if not p.get('ai_generated', True)])
                }
            }

        except Exception as e:
            logger.error(f"❌ Erro critico ao gerar provas visuais abrangentes: {e}")
            return {
                'success': False,
                'error': str(e),
                'fallback_provas': self._create_emergency_provas(avatar_data, context_data)
            }

    def _create_emergency_provas(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria provas de emergencia quando tudo falha"""
        segmento = context_data.get('segmento', 'mercado')
        produto = context_data.get('produto', 'produto')

        return {
            'prova_emergencia_1': self._create_basic_prova("Eficacia comprovada", segmento, produto),
            'prova_emergencia_2': self._create_basic_prova("Transformacao real", segmento, produto),
            'prova_emergencia_3': self._create_basic_prova("Resultados garantidos", segmento, produto)
        }

    def _validate_prova_quality(self, prova: Dict[str, Any], context_data: Dict[str, Any]) -> bool:
        """Valida a qualidade e relevância de uma prova visual"""
        if not prova:
            return False

        # Verifica se possui elementos essenciais
        required_keys = ['nome', 'conceito_alvo', 'tipo_prova', 'experimento', 'materiais', 'roteiro_completo', 'metricas_sucesso']
        if not all(key in prova for key in required_keys):
            logger.warning(f"Prova com chaves faltando: {prova.get('nome', 'Desconhecido')}")
            return False

        # Verifica se o conceito alvo está relacionado ao contexto
        segmento = context_data.get('segmento', '').lower()
        produto = context_data.get('produto', '').lower()
        conceito_alvo = prova.get('conceito_alvo', '').lower()

        if segmento and segmento not in conceito_alvo and \
           produto and produto not in conceito_alvo:
            logger.warning(f"Prova fora de contexto: {prova.get('nome', 'Desconhecido')}")
            return False

        # Verifica se há materiais e roteiro descritos
        if not prova.get('materiais') or not prova.get('roteiro_completo'):
            logger.warning(f"Prova sem materiais ou roteiro: {prova.get('nome', 'Desconhecido')}")
            return False

        return True

    def _generate_single_prova_with_ai(self, conceito: str, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Gera uma única prova visual usando IA"""
        try:
            segmento = context_data.get('segmento', 'negócios')
            produto = context_data.get('produto', 'produto')

            proof_type_info = self._select_best_proof_type(conceito, avatar_data)

            # Prompt para a IA
            prompt = f"""
Crie uma prova visual específica e convincente para o conceito: "{conceito}"

CONTEXTO:
- Segmento: {segmento}
- Produto: {produto}
- Avatar: Dores: {avatar_data.get('dores_viscerais', [])}, Desejos: {avatar_data.get('desejos_secretos', [])}

TIPO DE PROVA SUGERIDO: {proof_type_info['nome']}
OBJETIVO DA PROVA: {proof_type_info['objetivo']}
IMPACTO ESPERADO: {proof_type_info['impacto']}

FORMATO DE SAÍDA: JSON válido contendo as chaves:
- nome: Título da prova (Ex: "PROVI X: [Título Descritivo]")
- conceito_alvo: O conceito que a prova demonstra (igual ao input)
- tipo_prova: O tipo de prova selecionado (Ex: "{proof_type_info['nome']}")
- experimento: Descrição detalhada do que será demonstrado visualmente. Seja específico sobre os elementos visuais.
- materiais: Lista de materiais visuais necessários (Ex: ["Gráfico de barras comparativo", "Screenshot de dashboard", "Vídeo curto de depoimento"]). Seja específico.
- roteiro_completo: Dicionário com as chaves "preparacao", "execucao", "impacto_esperado". Descreva as etapas de forma clara e objetiva.
- metricas_sucesso: Lista de métricas para avaliar o sucesso da prova (Ex: ["Redução de objeções", "Aumento de engajamento"]).
- ai_generated: true (indica que foi gerado por IA)

AJUSTE O PROMPT PARA SER MAIS ESPECÍFICO E GERAR UM JSON MAIS DETALHADO E ACIONÁVEL.
Seja criativo e use os dados do avatar para personalizar a prova.
"""

            response = ai_manager.generate_analysis(prompt, max_tokens=1000)

            if response:
                # Limpeza da resposta da IA para extrair o JSON
                clean_response = response.strip()
                json_start = clean_response.find('```json')
                if json_start != -1:
                    json_start += 7
                    json_end = clean_response.rfind('```')
                    if json_end != -1:
                        clean_response = clean_response[json_start:json_end].strip()
                    else:
                        clean_response = clean_response[json_start:].strip()
                elif not clean_response.startswith('{'):
                    logger.warning(f"Resposta da IA não contém JSON esperado ou markdown para o conceito '{conceito}'. Resposta bruta: {response}")
                    return None

                try:
                    proof_data = json.loads(clean_response)
                    # Validação básica das chaves obrigatórias antes de retornar
                    if self._validate_prova_quality(proof_data, context_data):
                        proof_data['ai_generated'] = True # Marca como gerado por IA
                        return proof_data
                    else:
                        logger.warning(f"Prova gerada por IA falhou na validação interna para o conceito '{conceito}'.")
                        return None
                except json.JSONDecodeError as e:
                    logger.error(f"❌ Erro ao decodificar JSON da IA para o conceito '{conceito}': {e}. Resposta: {clean_response}")
                    logger.info(f"🔄 Gerando prova visual de fallback para '{conceito}'")
                    return self._generate_fallback_visual_proof(conceito, context_data)
            else:
                logger.warning(f"IA não retornou resposta para o conceito '{conceito}'.")
                return None

        except Exception as e:
            logger.error(f"Erro ao gerar prova visual com IA para o conceito '{conceito}': {e}")
            return None

    def _select_best_proof_type(self, concept: str, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Seleciona melhor tipo de prova para o conceito"""

        concept_lower = concept.lower()

        # Mapeia conceitos para tipos de prova
        if any(word in concept_lower for word in ['resultado', 'crescimento', 'melhoria', 'eficacia', 'performance']):
            return self.proof_types['antes_depois']
        elif any(word in concept_lower for word in ['concorrente', 'melhor', 'superior', 'diferencial']):
            return self.proof_types['comparacao_competitiva']
        elif any(word in concept_lower for word in ['tempo', 'rapidez', 'velocidade', 'progressao']):
            return self.proof_types['timeline_resultados']
        elif any(word in concept_lower for word in ['outros', 'clientes', 'pessoas', 'social', 'depoimento', 'confianca']):
            return self.proof_types['social_proof_visual']
        elif any(word in concept_lower for word in ['processo', 'metodo', 'como funciona', 'passo a passo']):
            return self.proof_types['demonstracao_processo']
        else: # Default caso nenhum seja encontrado
            return self.proof_types['demonstracao_processo']

    def _create_basic_prova(self, concept: str, segmento: str, produto: str) -> Dict[str, Any]:
        """Cria uma prova visual básica como fallback"""
        # Tenta associar um tipo de prova baseada no conceito, se possível
        proof_type_info = self._select_best_proof_type(concept, {}) # Avatar data não é essencial aqui

        return {
            'nome': f'PROVI: {proof_type_info["nome"]} para {produto}',
            'conceito_alvo': concept,
            'tipo_prova': proof_type_info['nome'],
            'experimento': f'Demonstração visual focada em "{concept}" para o {produto} no segmento de {segmento}.',
            'materiais': [
                f'Gráficos de {proof_type_info["nome"].lower()}',
                'Dados numéricos relevantes',
                'Screenshots de resultados',
                'Citações de clientes'
            ],
            'roteiro_completo': {
                'preparacao': f'Reunir dados e exemplos visuais que ilustrem "{concept}"',
                'execucao': f'Apresentar a prova de forma clara, conectando com os benefícios para o cliente',
                'impacto_esperado': 'Aumento da percepção de valor e confiança no produto'
            },
            'metricas_sucesso': [
                'Redução de objeções relacionadas a',
                'Aumento de interesse e engajamento',
                f'Confirmação de que "{concept}" é um benefício chave'
            ],
            'fallback_mode': True # Indica que é uma prova de fallback
        }

    def _get_default_visual_proofs(self, context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Retorna provas visuais padrão como fallback geral"""

        segmento = context_data.get('segmento', 'negócios')
        produto = context_data.get('produto', 'produto')

        return [
            {
                'nome': f'PROVI 1: Resultados Comprovados em {segmento}',
                'conceito_alvo': f'Eficácia da metodologia em {segmento}',
                'tipo_prova': 'Antes/Depois',
                'experimento': f'Comparação visual de resultados antes e depois da aplicação da metodologia em {segmento}',
                'materiais': ['Gráficos de crescimento', 'Dados de performance', 'Screenshots de métricas'],
                'roteiro_completo': {
                    'preparacao': 'Organize dados de clientes que aplicaram a metodologia',
                    'execucao': 'Mostre transformação clara com números específicos',
                    'impacto_esperado': 'Convencimento através de evidência visual'
                },
                'metricas_sucesso': ['Redução de ceticismo', 'Aumento de interesse']
            },
            {
                'nome': f'PROVI 2: Comparação com Mercado em {segmento}',
                'conceito_alvo': f'Superioridade da abordagem em {segmento}',
                'tipo_prova': 'Comparação Competitiva',
                'experimento': f'Comparação visual entre abordagem tradicional e metodologia específica para {segmento}',
                'materiais': ['Tabelas comparativas', 'Gráficos de performance', 'Benchmarks do setor'],
                'roteiro_completo': {
                    'preparacao': 'Colete dados de mercado e benchmarks',
                    'execucao': 'Apresente comparação lado a lado',
                    'impacto_esperado': 'Demonstração clara de vantagem competitiva'
                },
                'metricas_sucesso': ['Compreensão do diferencial', 'Justificativa de preço premium']
            },
            {
                'nome': f'PROVI 3: Depoimentos Visuais {segmento}',
                'conceito_alvo': f'Validação social no {segmento}',
                'tipo_prova': 'Prova Social Visual',
                'experimento': f'Compilação visual de depoimentos de profissionais de {segmento}',
                'materiais': ['Vídeos de depoimento', 'Screenshots de resultados', 'Fotos de clientes'],
                'roteiro_completo': {
                    'preparacao': 'Selecione melhores depoimentos com resultados',
                    'execucao': 'Apresente sequência de validações sociais',
                    'impacto_esperado': 'Redução de risco percebido'
                },
                'metricas_sucesso': ['Aumento de confiança', 'Redução de objeções']
            }
        ]

    def _generate_fallback_visual_proof(self, conceito: str, contexto: Dict[str, Any]) -> Dict[str, Any]:
        """Gera prova visual de fallback quando IA falha"""

        fallback_proofs = {
            'Eficacia do produto': {
                'tipo': 'Comparação Visual',
                'descricao': f'Demonstração prática da eficácia do {contexto.get("produto", "produto")}',
                'elementos': ['Antes vs Depois', 'Métricas de performance', 'Resultados mensuráveis'],
                'impacto_psicologico': 'Alto - prova tangível de resultados'
            },
            'Credibilidade da empresa': {
                'tipo': 'Prova Social',
                'descricao': 'Evidências da credibilidade e autoridade da empresa',
                'elementos': ['Certificações', 'Depoimentos', 'Cases de sucesso'],
                'impacto_psicologico': 'Alto - constrói confiança imediata'
            },
            'Qualidade superior': {
                'tipo': 'Demonstração Comparativa',
                'descricao': 'Comparação visual da qualidade superior',
                'elementos': ['Materiais premium', 'Processos diferenciados', 'Acabamento superior'],
                'impacto_psicologico': 'Médio-Alto - justifica valor premium'
            }
        }

        return fallback_proofs.get(conceito, {
            'tipo': 'Demonstração Geral',
            'descricao': f'Prova visual para {conceito}',
            'elementos': ['Evidência tangível', 'Comparação', 'Validação'],
            'impacto_psicologico': 'Médio - suporte visual ao argumento',
            'is_fallback': True
        })

# Instância global
visual_proofs_generator = VisualProofsGenerator()