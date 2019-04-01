import { Injectable } from '@angular/core';
import { User } from '../models/user';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { Observable } from 'rxjs/Observable';
import { resolve } from 'q';
import { News } from '../models/news';

@Injectable()
export class UserService {

  private _news: BehaviorSubject<News[]>;

  private dataStore: {
    news: News[]
  }

  constructor(private http: HttpClient) {
    this.dataStore = { news: [] };
    this._news = new BehaviorSubject<News[]>([]);
  }

  get news(): Observable<News[]> {
    return this._news.asObservable();
  }

  // addUser(user: User): Promise<User> {
  //   return new Promise((resolver, reject) => {
  //     user.id = this.dataStore.news.length + 1;
  //     this.dataStore.news.push(news);
  //     this._news.next(Object.assign({}, this.dataStore).users);
  //     resolver(user);
  //   });
  // }

  newsByTitle(title: string) {
    return this.dataStore.news.find(x => x.title == title);
  }

  loadAll() {
    const usersUrl = 'http://localhost:4200/assets/news.json';

    return this.http.get<News[]>(usersUrl)
      .subscribe(data => {
        this.dataStore.news = data;
        this._news.next(Object.assign({}, this.dataStore).news);
      }, error => {
        console.log("Failed to fetch users");
      });
  }

}
