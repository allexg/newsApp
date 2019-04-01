import { Component, OnInit } from '@angular/core';
import { User } from '../../models/user';
import { ActivatedRoute } from '@angular/router';
import { UserService } from '../../services/user.service';
import { News } from '../../models/news';

@Component({
  selector: 'app-main-content',
  templateUrl: './main-content.component.html',
  styleUrls: ['./main-content.component.scss']
})
export class MainContentComponent implements OnInit {

  news: News;
  constructor(
    private route: ActivatedRoute,
    private service: UserService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      let title = params['id'];
      if (!title) title = 'Linda McMahon to step down as head of Small Business Administration, source says - Fox News';
      this.news = null;

      this.service.news.subscribe(news => {
        if (news.length == 0) return;

        setTimeout(() => {
          this.news = this.service.newsByTitle(title);
        }, 500);
      });

    })
  }

}
