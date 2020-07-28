#define MAX_BUF_SIZE 128
typedef struct server_socket {
        int *srv_token;
} server_socket;
int read_from_input() {return 100;}      /* read an integer from the enviornment */
void buffer_init(server_socket* srv_socket)
{
}
void buffer_copy_string_buffer(char* to, int* from)
{
  for(int i = 0; i < MAX_BUF_SIZE; i++)
    to[i] = from[i]; /* BUFFER OVERFLOW */
}
int main ()
{
  server_socket *srv_socket = malloc(sizeof(srv_socket));
  char string[100];
  srv_socket->srv_token = (int *)malloc(sizeof(int)*MAX_BUF_SIZE);
  buffer_copy_string_buffer(string, srv_socket->srv_token);
}