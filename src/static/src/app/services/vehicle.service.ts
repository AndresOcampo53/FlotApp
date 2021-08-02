import { Injectable } from '@angular/core';

@Injectable()
export class VehicleService {

    private vehicle: Vehicle[] = [
        {
            placa: "STQ125",
            modelo: "KODIAK 1998",
            capacidad: 20,
            kilometraje: 81.562,
            centro_operaciones_id: "Manizales"
        },
        {
            placa: "NAM987",
            modelo: "KENWORTH 2015",
            capacidad: 21,
            kilometraje: 67.980,
            centro_operaciones_id: "Manizales"
        },
        {
            placa: "MAN886",
            modelo: "CHEVROLET 2006",
            capacidad: 21,
            kilometraje: 85.345,
            centro_operaciones_id: "Manizales"
        },
        {
            placa: "MZR198",
            modelo: "CHEVROLET 2010",
            capacidad: 1,
            kilometraje: 98.076,
            centro_operaciones_id: "Manizales"
        },
        {
            placa: "RFD098",
            modelo: "KENWORTH 2015",
            capacidad: 20,
            kilometraje: 40.783,
            centro_operaciones_id: "Manizales"
        },
        {
            placa: "EFL983",
            modelo: "KENWORTH 2017",
            capacidad: 20,
            kilometraje: 20.034,
            centro_operaciones_id: "Manizales"
        },
        {
            placa: "EFP349",
            modelo: "KENWORTH 2016",
            capacidad: 21,
            kilometraje: 21.238,
            centro_operaciones_id: "Manizales"
        }
    ];

    constructor() {
        
    }

    geVehicle():Vehicle[]{
        return this.vehicle;
      }

}

export interface Vehicle {
    placa: string,
    modelo: string,
    capacidad: number,
    kilometraje: number,
    centro_operaciones_id: string
};
