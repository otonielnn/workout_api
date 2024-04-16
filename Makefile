# Criando commando reduzido para subir o servidor
run:
	@uvicorn workout_api.main:app --reload