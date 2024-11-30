const request = require('supertest');
const app = require('../server');

describe('Auth API', () => {
    it('should return 200 for login endpoint', async () => {
        const res = await request(app).post('/api/auth/login').send({
            email: 'test@example.com',
            password: 'password123',
        });
        expect(res.statusCode).toEqual(200);
        expect(res.body).toHaveProperty('token');
    });
});