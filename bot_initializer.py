# Declaracao e inicializacao das variaveis
BOT_NAME = "RPA_FINANCEIRO_01"
MAX_RETRIES = 3
EXECUTION_TIMEOUT = 120.5
IS_PRODUCTION = False

# Mensagem de inicializacao formatada
print("=" * 50)
print("🚀 INICIALIZANDO O BOT")
print("=" * 50)
print(f"BOT_NAME: {BOT_NAME} (Tipo: {type(BOT_NAME).__name__})")
print(f"MAX_RETRIES: {MAX_RETRIES} (Tipo: {type(MAX_RETRIES).__name__})")
print(f"EXECUTION_TIMEOUT: {EXECUTION_TIMEOUT} (Tipo: {type(EXECUTION_TIMEOUT).__name__})")
print(f"IS_PRODUCTION: {IS_PRODUCTION} (Tipo: {type(IS_PRODUCTION).__name__})")
print("=" * 50)