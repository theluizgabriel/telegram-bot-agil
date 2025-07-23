import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';  // URL do seu backend FastAPI

  constructor(private http: HttpClient) { }

  getMessages() {
    return this.http.get(`${this.apiUrl}/messages`);
  }
}