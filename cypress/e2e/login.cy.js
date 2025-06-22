describe('User Login Page', () => {
  it('allows a user to log in with valid credentials', () => {
    cy.visit('/login');
    cy.get('input[name=email]').type('test@example.com');
    cy.get('input[name=password]').type('password123');
    cy.get('button[type=submit]').click();
    // Should redirect to dashboard or show logged in state
    cy.url().should('not.include', '/login');
  });
});
