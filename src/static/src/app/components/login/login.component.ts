import { Component, OnInit } from '@angular/core';
import { FormControl, NgForm, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UsuarioModel } from 'src/app/models/usuario.model';
import { AuthService } from 'src/app/services/auth.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor( private auth: AuthService, private router: Router ) { 
    
  }
  
  EmailControl = new FormControl('', [Validators.required]);
  PasswordControl = new FormControl('', [Validators.required]);
  usuario: UsuarioModel = new UsuarioModel();
  
  ngOnInit() {
  } 

  onSubmit( form: NgForm ){

    if (form.invalid) {
      return;
    }

    Swal.fire({
      icon: 'info',
      allowOutsideClick: false,
      text: 'Espere por favor...'      
    });

    Swal.showLoading();

    this.auth.login( this.usuario ).subscribe(
      resp => {
        console.log(resp);
        Swal.close();
        this.router.navigateByUrl('/user');
        
      }, (err) => {
        console.log(err.error.error.message);
        Swal.fire({
          icon: 'error',
          title: 'Error al autenticar',          
          text: err.error.error.message     
        });
      });
  }

}
