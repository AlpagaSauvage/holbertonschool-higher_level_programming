#include "hash_tables.h"

/**
 * key_index - give index of key
 * @key: key of hash
 * @size: size of hash
 * Return: hash_djb2(key) % size
 */

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
