export interface Llantas {
    id: number,
    vehiculo_id: number,
    marca: string,
    posicion: number,
    profundidad: number,
    kilometraje_instalacion_llanta: number,
    fecha_instalacion_llanta: Date,
    kilometraje_descarte_llanta: number,
    fecha_descarte_llanta: Date,
    motivo_descarte: string
}