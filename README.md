# stream-cipher-example

Preguntas:
1. ¿Cómo cambia el mensaje cifrado cuando cambias la clave?

    R// En este caso para cada cambio de llave se puede notar que existen distintos resultados de cifrados, esto se debe a la forma en la que se realiza con la aleatoridad de la creación de las llaves por medio del keystream.

2. ¿Qué sucede si utilizas el mismo Keystream para cifrar dos mensajes diferentes?

    R// Para este caso se debe de tomar en cuenta que se debe de tener la misma longitud de mensajes, debido a esta restricción se si logran encontrar dos mensajes distintos de la misma longitud se puede ver que la forma en la que se cifra, el resultado que se puede obtener es bastante distinto entre los mensajes.

3. ¿Cómo afecta la longitud del Keystream a la seguridad del cifrado?

    R// En este caso debido a la forma de aleatoriedad del cifrado puede mejorar en como se llega a cifrar un mensaje, en este caso una desventaja puede llegar a ser que al momento de enviar o compartir la clave puede llegar a ser una longitud muy grande debido a la forma en la que funciona.