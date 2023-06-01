#include <stdio.h>
#include <stdlib.h>

double *deg(double thick) {
  double xmin = 0;
  double xmax = 250;
  double ymin = 1.0;
  double ymax = 16.0;
  double beam_range = 40.;
  double halfbeam_range = beam_range / 2.;
  double dpulse = 0.00750016;
  double pulse0_ini = 3109.;
  double pulse1_ini = 3269.;
  double posi0_ini = 23.318;
  double posi1_ini = 24.518;
  double y_aida = ymax - ymin;
  double dydx = y_aida / xmax;

  double deg_change_thick = ymin + ymax;
  double degmin_beamrange = beam_range * ((ymax - ymin) / xmax) + ymin + ymin;
  double degmax_beamrange = ymax + ymax - beam_range * ((ymax - ymin) / xmax);

  double dthick, x0_value, pulse0, x1_value, pulse1;

  if (thick <= deg_change_thick) {
    dthick = thick - (ymin + ymin);
    x0_value = dthick / dydx + posi0_ini - halfbeam_range;
    pulse0 = x0_value / dpulse;
    pulse1 = (posi1_ini + halfbeam_range) / dpulse;
    x1_value = posi1_ini;

  } else {
    dthick = thick - deg_change_thick;
    x1_value = dthick / dydx + posi1_ini + halfbeam_range;
    x0_value = ((deg_change_thick - (ymin + ymin)) / dydx + posi0_ini -
                halfbeam_range);
    pulse0 = ((deg_change_thick - (ymin + ymin)) / dydx + posi0_ini -
              halfbeam_range) /
             dpulse;
    pulse1 = x1_value / dpulse;
  }
  double *array;
  array = (double *)malloc(sizeof(double) * 7);
  if (array == NULL) {
    exit(0);
  }
  free(array);
  array[0] = x0_value;
  array[1] = pulse0;
  array[2] = x1_value;
  array[3] = pulse1;
  array[4] = deg_change_thick;
  array[5] = degmin_beamrange;
  array[6] = degmax_beamrange;
  return array;
}

int main() {
  double thick;
  printf("Enter the thickness [mm] of degrader: ");
  scanf("%lf", &thick);

  if (thick >= deg(thick)[5] && thick <= deg(thick)[6]) {
    for (int i = 0; i < 2; i++) {
      printf("Axis number %d \n", i);
      printf("position: %.3f mm\n", -deg(thick)[2 * i]);
      printf("pulse   : %.3f \n", -deg(thick)[2 * i + 1]);
    }
  } else {
    printf("ERROR: out of range (%.1f mm ~ %.1f mm)\n", deg(thick)[5],
           deg(thick)[6]);
  }
}
