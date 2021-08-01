import { ClassGetter } from '@angular/compiler/src/output/output_ast';
import { Component, OnInit } from '@angular/core';
import { FormControl, NgForm, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UsuarioModel } from 'src/app/models/usuario.model';
import { AuthService } from 'src/app/services/auth.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {  

  NameControl = new FormControl('', [Validators.required]);
  PasswordControl = new FormControl('', [Validators.required]);
  EmailControl = new FormControl('', [Validators.required, Validators.email]);
  usuario: UsuarioModel = new UsuarioModel();

  constructor( private auth: AuthService, private router: Router ) { 
    
  }

  ngOnInit(): void {
    //this.usuario = new UsuarioModel();

    //this.usuario.username = 'test';
  }

  onSubmit(form:NgForm){

    if (form.invalid) {
      return;
    }

    Swal.fire({
      icon: 'info',
      allowOutsideClick: false,
      text: 'Espere por favor...'      
    });

    Swal.showLoading();

    this.auth.newuser(this.usuario).subscribe(
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
