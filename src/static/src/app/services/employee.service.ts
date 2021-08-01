import { Injectable } from '@angular/core';

@Injectable()
export class EmployeeService {

    private employee: Employee[] = [
        {
            nombre: "Pedro perez",
            bio: "Conductor",
            aparicion: "08-09-1960",
            cedula: "10.987.654"
        },
        {
            nombre: "Luis Evelio Marulanda",
            bio: "Conductor",
            aparicion: "09-05-1976",
            cedula: "18.876.123"
        },
        {
            nombre: "Ricardo Franco",
            bio: "Conductor",
            aparicion: "11-07-1968",
            cedula: "17.908.654"
        },
        {
            nombre: "Alexander Gracia",
            bio: "Conductor",
            aparicion: "12-04-1970",
            cedula: "11.234.874"
        },
        {
            nombre: "Jesus Pineda",
            bio: "Conductor",
            aparicion: "03-09-1976",
            cedula: "17.897.223"
        },
        {
            nombre: "Juan Carlos Rojas",
            bio: "Conductor",
            aparicion: "11-09-1987",
            cedula: "70.854.123"
        },
        {
            nombre: "Andres Ocampo",
            bio: "Administrador",
            aparicion: "04-23-1992",
            cedula: "1.053.987.921"
        }
    ];

    constructor() {
        console.log("Servicio listo para usar!!!");
    }

    geEmployee():Employee[]{
        return this.employee;
      }

}

export interface Employee {
    nombre: string;
    bio: string;
    aparicion: string;
    cedula: string;
    idx?: number;
};
