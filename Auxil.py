/*
*   Erick Eduardo López Nava
*
*   Link de grafica:
*   https://drive.google.com/file/d/1bl6l6rrej2GfS8oUcguKVIThlYw1HJgH/view?usp=sharing
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
#define DEFAULT_POINTS      100000

int     num_threads;                        /* threads to be create.                        */
int     work_per_thread;                    /* amount of work to be done by each thread.    */
long    circle_count;                       /* points inside circle.                        */
long    points;                             /* points to be launch.                         */
unsigned int seed;                          /* seed to rand_r (thread safe)                 */

/*
*   Creates a random number in range [0,1]
*/
double rndm(){
  return (double)rand_r(&seed) / (double)((unsigned) + 1);
}

/*
*   Do the Monte Carlo calculation for pi
*   Uses a count_in to keep track of the circle_count in each thread
*/
void *pical(void *t_id){
  double x, y;
  int *count_in = (int *)malloc(sizeof(int));
  *count_in = 0;

  int i;
  for(i=0; i<work_per_thread; i++){
      x = rndm();
      y = rndm();
      if( pow((x),2) + pow((y),2) <= 1)
          *count_in += 1;
  }
  pthread_exit((void *) count_in);
}

int main(int argc, const char* argv[]){
  //clock_t begin = clock();
  seed = time(NULL);
  points = DEFAULT_POINTS;

  if(strcmp("-num-threads", argv[1]) == 0) {
      /*********************************************************************************************/
      num_threads = atoi(argv[2]);
      if(num_threads == 0){
          printf( "Error: -num-threads must be greater than 0\n");
          exit(1);
      }
          printf("-------------------------------------------------\n"
                 " Working with -num-threads -> %d \n"
                 " Points to be launch       -> %zd \n"
                 "-------------------------------------------------\n", num_threads, points);
      /*********************************************************************************************/
}
  double  pi;
  void    *count_inside_thread;
  int     thread_creation;

  pthread_t threads[num_threads];                 /* Create the array of threads */
  work_per_thread = points / num_threads;

  printf("Doing %d points per thread\n", work_per_thread);
  /*
  *   Create the threads up to num_threads
  */
  unsigned int i;
  for(i=0; i<num_threads; i++){
      thread_creation = pthread_create(&threads[i], NULL, pical, (void *)(intptr_t) i);
      seed++;
      thread_creation ? exit(1) : printf("Thread %i create correctly\n", i);
  }
  /*
  *   Main() waits for threads to be completed
  *   Returns the count for each thread and sums it all
  */
  for(i=0; i<num_threads; i++){
      pthread_join(threads[i], &count_inside_thread);
      circle_count += * (long *) count_inside_thread;
  }

  printf("-------------------------------------------------\n"
         "Total points launched: %zd\n"
         "Total inside circle: %zd\n", points, circle_count);

  pi = (4.00 * (float)circle_count) / (float)points;

  printf("\nPi-> %.5f\n", pi);

  //clock_t end = clock();
  //double time_spent = (double)(end-begin) / CLOCKS_PER_SEC;
  //printf("-------------------------------------------------\n"
  //       "Time used with %d threads and %zd points --> %.3f\n", num_threads, points, time_spent);
  exit(0);
}
