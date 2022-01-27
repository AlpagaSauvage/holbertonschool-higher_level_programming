#include "hash_tables.h"

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new_hash;

	new_hash = malloc(sizeof(hash_table_t) * size);

	return (new_hash);
}
