#define MAX_BUF_SIZE 128
typedef struct server_socket {
        int       fde_ndx;
        int *srv_token;
} server_socket;
int read_from_input() {return 100;}      /* read an integer from the enviornment */
void buffer_init(server_socket* srv_socket)
{
  for (int i = 0;i < MAX_BUF_SIZE;i++)
    srv_socket->srv_token[i] = 0;
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
  int delim = read_from_input();
  srv_socket->srv_token = (int *)malloc(sizeof(int)*MAX_BUF_SIZE);
  buffer_init(srv_socket);
  buffer_copy_string_buffer(string, srv_socket->srv_token);
  {
    string[delim] = '\0';
    delim++;
  }
}