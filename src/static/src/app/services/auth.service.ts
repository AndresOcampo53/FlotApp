import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { pipe } from 'rxjs';
import { UsuarioModel } from '../models/usuario.model';
import { map } from 'rxjs/operators';
import Swal from 'sweetalert2';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private url = 'https://identitytoolkit.googleapis.com/v1/accounts';
  private apikey = 'AIzaSyDelQyGw-GYYcOecPlgAroAnQwCppr0Q94';
  userToken : any;

  //crear nuevos usuarios
  //https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[API_KEY]

  //iniciar sesion
  //https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[API_KEY]

  constructor( private http: HttpClient) {    
  }

  logout(){}

  login(usuario: UsuarioModel){
    const authData = {
      email: usuario.email,
      password: usuario.password,
      returnSecureToken: true
    };

    return this.http.post(
      `${ this.url }:signInWithPassword?key=${ this.apikey }`,
      authData
    ).pipe(
      map( resp => {
        this.guardarToken( resp.toString() )
        return resp;
      } )
    );
  }

  newuser(usuario: UsuarioModel){
    const authData = {
      email: usuario.email,
      password: usuario.password,
      returnSecureToken: true
    };

    return this.http.post(
      `${ this.url }:signUp?key=${ this.apikey }`,
      authData
      ).pipe(
        map( resp => {
          this.guardarToken( resp.toString() )
          return resp;
        } )
      );
  }

  private guardarToken( idToken: string ){
    this.userToken = idToken;
    localStorage.setItem('token', idToken);
  }

  leerToken(){
    if (localStorage.getItem('token')) {
      this.userToken = localStorage.getItem('token');
    } else {
      this.userToken = '';
    }

    return this.userToken;
  }

}
